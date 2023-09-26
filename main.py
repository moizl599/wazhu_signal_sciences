import json
import os
import glob
from SigSciApiPy.SigSci import SigSciAPI


class SignalScience:
    def __init__(self, config_file='key.cfg'):
        """
        Initializes SignalScience object with required configurations and parameters from the config file.

        :param config_file: The path to the configuration file. Default is 'key.cfg'.
        """
        with open(config_file) as f:
            config = json.load(f)

        self.sigsci = SigSciAPI()
        self.sigsci.email = config['email']
        self.sigsci.corp = config['corp']
        self.sigsci.site = config['site']
        self.sigsci.api_token = config['api_token']
        self.tags = config['tags']
        self.sigsci.from_time = config.get('from_time', '-5min')  # Defaults to '-5min' if not provided in config file

    def run(self):
        """
        Executes the API call to fetch events, logs events per tag and then merges all log files into a master log file.
        """
        if self.sigsci.authenticate():
            for tag in self.tags:
                logfile = f"/opt/wazuh_logging/signal_science/logfiles/{tag}_logs.log"

                # Remove existing log file
                if os.path.isfile(logfile):
                    os.remove(logfile)

                # Open the log file and write events fetched from API
                with open(logfile, 'a') as logs_file:
                    events = self.sigsci.get_list_events(tag)['data']
                    for event in events:
                        res = {key: event[key] for key in {'timestamp', 'source', 'remoteCountryCode', 'action', 'reasons'}}
                        log_entry = {
                            'WAF_timestamp': res.get('timestamp', ''),
                            'WAF_source': res.get('source', ''),
                            'WAF_Remote_country': res.get('remoteCountryCode', ''),
                            'WAF_action': res.get('action', ''),
                            'WAF_reason': res.get('reasons', ''),
                        }
                        json.dump(log_entry, logs_file)
                        logs_file.write('\n')

            # Merge all individual log files into a master log file
            master_logfile = '/opt/wazuh_logging/signal_science/masterlogfile/master_logfile.log'
            if os.path.isfile(master_logfile):
                os.remove(master_logfile)

            files = glob.glob('/opt/wazuh_logging/signal_science/logfiles/*.log')
            with open(master_logfile, 'w') as result:
                for file in files:
                    with open(file, 'r') as f:
                        for line in f:
                            result.write(line)


def main():
    """
    The main function to instantiate the SignalScience object and run the event fetching and logging.
    """
    signal_science = SignalScience()
    signal_science.run()


if __name__ == "__main__":
    main()
