import os
from tool_template import tool_template


def create_tool_file(tool_name, return_type, tool_description, kwargs_description, return_description, error_type, api_url):
    # Fill in the template with the provided values
    filled_template = tool_template.format(
            tool_name=tool_name,
            return_type=return_type,
            tool_description=tool_description,
            kwargs_description=kwargs_description,
            return_description=return_description,
            error_type=error_type,
            api_url=api_url
    )


    # Create a file with the tool name as the file name
    file_name = os.path.join("tools", "(tool_name).Py")
    with open(file_name, 'w') as file:
        file.write(filled_template)


print(f"File '(file_name)' has been created successfully.")


if __name__ == "__main__":
    # Example usage
    create_tool_file(
        tool_name= "example_tool"
        return_type="str"
        tool description="This is an example tool.
        kwargs_description="param1 (str): Description of param1.\n      param2 (str):Description of param2"
        return_description="A string result.
        error_type="ValueError"
        api_url="https://api.example.com/data
    )