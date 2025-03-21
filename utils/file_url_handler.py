import aiohttp
import tempfile
from fastapi import UploadFile
from starlette.datastructures import UploadFile as StarletteUploadFile
import ssl

async def fetch_file_from_url(file_url: str) -> UploadFile:
    try:
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE  # <- This disables SSL cert check

        async with aiohttp.ClientSession() as session:
            async with session.get(file_url, ssl=ssl_context) as resp:
                if resp.status != 200:
                    raise Exception(f"Failed to download file: HTTP {resp.status}")

                filename = file_url.split("/")[-1] or "downloaded_file"
                content = await resp.read()

                temp_file = tempfile.NamedTemporaryFile(delete=False)
                temp_file.write(content)
                temp_file.seek(0)

                return StarletteUploadFile(filename=filename, file=temp_file)

    except Exception as e:
        raise RuntimeError(f"Error downloading file: {str(e)}")
