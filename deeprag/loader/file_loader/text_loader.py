from typing import List
from langchain_core.documents import Document
from deeprag.loader.file_loader.base import BaseLoader


class TextLoader(BaseLoader):
    def __init__(self):
        pass

    def load_file(self, file_path: str) -> List[Document]:
        with open(file_path, "r") as f:
            return [Document(page_content=f.read(), metadata={"source": file_path})]
    
    @property
    def supported_file_types(self) -> List[str]:
        return ["txt", "md"]
