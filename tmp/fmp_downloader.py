import os
import pathlib
from fmp_api import FMPapi


class FMPDownloader(FMPapi):
    def download_csv(self, statement_name: str) -> bool:
        """
        Write content to CSV in Home/Downloads folder
        :return: None
        """
        try:
            home_dir = pathlib.Path.home()
            file_path = os.path.join(
                home_dir,
                "Downloads",
                f'{self.ticker}_{statement_name}.csv'
            )

            with open(file_path, "w") as file:
                file.write(self.get_cash_flow_statement_download().content.decode('utf-8'))
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

