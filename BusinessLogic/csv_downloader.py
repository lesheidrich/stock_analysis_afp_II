import os
import pathlib
from fmp_api import FMPApi


class CSVDownloader(FMPApi):
    def download_from_fmp_api(self, response_content) -> None:
        """
        Write content to CSV in Home/Downloads folder
        :return: None
        """
        if response_content["message"] == "success":
            home_dir = pathlib.Path.home()
            file_path = os.path.join(
                home_dir,
                "Downloads",
                f'{self.ticker}_{response_content["type"]}.csv'
            )

            with open(file_path, "w") as file:
                file.write(response_content["content"])
        else:
            raise Exception("Unable to write CSV content")
