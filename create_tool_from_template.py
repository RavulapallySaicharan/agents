from tool_template import tool_template


1
2
3


سنه


##


def create_tool_file(tool_name, return type, tool_description, kwargs_description,
return_description, error_type, api_url):
# Define the template


# Fill in the template with the provided values


filled_template
tool template. forma
tool name=tool_ name,
return_type=return_type,
tool_description-tool_description,
kwargs_description=kwargs_description,
I
return_description=return_description,
error_type=error _type,
api_ url-api url


# Create a file with the tool name as the file name
file_name = os.path.join("tools", "(tool_name).Py")
with open(file_name, 'w') as file:
file.write(filled_template)


print(f"File '(file_name)' has been created successfully.")
