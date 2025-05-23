#!/usr/bin/env python3
"""
This script populates all files in the INDUSTRIAL-LIMS project with default header comments.
Each file will have a header generated based on its type and location (module),
referencing ReadMe.md for project structure and details.
"""

import os


def get_default_content(file_path):
    """
    Returns a default header content based on the file extension and its directory.
    """
    parts = file_path.split(os.sep)
    description = ""
    if "INDUSTRIAL-LIMS" in parts:
        idx = parts.index("INDUSTRIAL-LIMS")
        if len(parts) > idx + 1 and parts[idx + 1] == "app":
            description = "App module for initializing the project."
        elif len(parts) > idx + 1 and parts[idx + 1] == "modules":
            # Next item under modules is the module name
            module_name = parts[idx + 2] if len(parts) > idx + 2 else "Unknown Module"
            description = f"{module_name.capitalize()} module of INDUSTRIAL-LIMS."
        else:
            description = "INDUSTRIAL-LIMS project file."
    else:
        description = "Project file."
    
    filename = os.path.basename(file_path)
    
    if file_path.endswith(".py"):
        content = f"#!/usr/bin/env python3\n" \
                  f"\"\"\"\n{filename} - {description}\n" \
                  f"Reference: See ReadMe.md for project details.\n\"\"\"\n\n"
    elif file_path.endswith(".html"):
        content = f"<!-- {filename} - {description} | Reference: ReadMe.md -->\n"
    elif file_path.endswith(".js"):
        content = f"// {filename} - {description} | Reference: ReadMe.md\n"
    elif file_path.endswith(".css"):
        header = f"/* {filename} - {description} | Reference: ReadMe.md */\n"
        standard_css = (
            "/* Standard CSS Reset for INDUSTRIAL-LIMS */\n"
            "html, body, div, span, applet, object, iframe,\n"
            "h1, h2, h3, h4, h5, h6, p, blockquote, pre,\n"
            "a, abbr, acronym, address, big, cite, code,\n"
            "del, dfn, em, img, ins, kbd, q, s, samp,\n"
            "small, strike, strong, sub, sup, tt, var,\n"
            "b, u, i, center,\n"
            "dl, dt, dd, ol, ul, li,\n"
            "fieldset, form, label, legend,\n"
            "table, caption, tbody, tfoot, thead, tr, th, td,\n"
            "article, aside, canvas, details, embed,\n"
            "figure, figcaption, footer, header, hgroup,\n"
            "menu, nav, output, ruby, section, summary,\n"
            "time, mark, audio, video {\n"
            "    margin: 0;\n"
            "    padding: 0;\n"
            "    border: 0;\n"
            "    font-size: 100%;\n"
            "    font: inherit;\n"
            "    vertical-align: baseline;\n"
            "}\n"
            "article, aside, details, figcaption, figure,\n"
            "footer, header, hgroup, menu, nav, section {\n"
            "    display: block;\n"
            "}\n"
            "body {\n"
            "    line-height: 1;\n"
            "}\n"
            "ol, ul {\n"
            "    list-style: none;\n"
            "}\n"
            "blockquote, q {\n"
            "    quotes: none;\n"
            "}\n"
            "blockquote:before, blockquote:after,\n"
            "q:before, q:after {\n"
            "    content: '';\n"
            "    content: none;\n"
            "}\n"
            "table {\n"
            "    border-collapse: collapse;\n"
            "    border-spacing: 0;\n"
            "}\n"
        )
        content = header + standard_css
    else:
        content = f"{filename} - {description}\nReference: ReadMe.md\n"
    return content


def populate_files(base_dir):
    """
    Walk through the given base directory and populate each file with a default header.
    """
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            content = get_default_content(file_path)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Populated {file_path}")


def main():
    base_directory = os.path.join(os.getcwd(), "INDUSTRIAL-LIMS")
    if not os.path.exists(base_directory):
        print(f"Directory {base_directory} does not exist. Please run generate_project_structure.py first.")
        return
    populate_files(base_directory)


if __name__ == "__main__":
    main() 