import os


class StaticContent:
    def __init__(self, content, content_type):
        self.content = content
        self.content_type = content_type
 

class StaticContentProvider:
    def __init__(self, static_data_folder, content_types):
        self.STATIC_DATA_FOLDER = static_data_folder
        self.SUPPORTED_CONTENT_TYPES = content_types 

    def __resource_exists(self, resource: str) -> bool:
        return os.path.exists(resource)
    
    
    def __build_resource_path(self, resource: str) -> str:
        return os.path.join(self.STATIC_DATA_FOLDER, resource[1:])
    
    
    def __fetch_resource(self, full_resource_path: str) -> bytes | None:
        """Fetches the content from the content from the resource and sends it as bytes."""
    
        fp = None
    
        fp = open(file=full_resource_path, mode='rb')
    
        content = fp.read()
        fp.close()
    
        return content
    
    
    def __get_resource_content_type(self, resource) -> str | None:
        """Gets the content type of resource."""
    
        file_format = ""
    
        i = len(resource)-1
    
        while ((c := resource[i]) != "."):
            file_format = c + file_format 
            i -= 1
    
        if file_format not in self.SUPPORTED_CONTENT_TYPES:
            return None
    
        return self.SUPPORTED_CONTENT_TYPES[file_format]


    def resolve(self, resource) -> StaticContent | None:

        full_resource_path = self.__build_resource_path(resource)

        if not self.__resource_exists(full_resource_path):
            return None

        content_type = self.__get_resource_content_type(full_resource_path)
        content = self.__fetch_resource(full_resource_path)

        return StaticContent(content, content_type)
    

