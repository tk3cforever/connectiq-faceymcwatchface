import json


GENERATED_FILE_WARNING = "This is a generated file. Do not edit manually or suffer the consequences..."




#     #                                        
#     # ##### # #      # ##### # ######  ####  
#     #   #   # #      #   #   # #      #      
#     #   #   # #      #   #   # #####   ####  
#     #   #   # #      #   #   # #           # 
#     #   #   # #      #   #   # #      #    # 
 #####    #   # ###### #   #   # ######  ####  

def add_index_field(items):
    """Adds an index field to all dictionaries in the given list of dictionaries."""

    for index, item in enumerate(items):
        item["index"] = index


def sorted_by_localized_name(items):
    """Returns a view on the given items that is sorted by their English language names."""

    return sorted(
        items,
        key=lambda item: item["languages"]["en"])


def to_file_name_suffix(config):
    """Generates the suffix to be used for output files."""

    return F"_{config['category'].lower()}s"


def to_drawable_id(config, id):
    """Generates an identifier to be used for the given drawable ID."""

    return F"{config['category']}{id}"


def to_behavior_id(config, id):
    """Generates an identifier to be used for the given behavior ID."""

    return F"{config['category']}Behavior{id}"




######                                                          
#     # #####    ##   #    #   ##   #####  #      ######  ####  
#     # #    #  #  #  #    #  #  #  #    # #      #      #      
#     # #    # #    # #    # #    # #####  #      #####   ####  
#     # #####  ###### # ## # ###### #    # #      #           # 
#     # #   #  #    # ##  ## #    # #    # #      #      #    # 
######  #    # #    # #    # #    # #####  ###### ######  ####  

def generate_drawables(config):
    """Generate the drawables for the given config."""

    with open(F"resources/drawables/drawables{to_file_name_suffix(config)}.xml", mode="w", encoding="utf8", newline="\n") as out_file:
        print(F"<!-- {GENERATED_FILE_WARNING} -->", file=out_file)
        print(F"<drawables>", file=out_file)

        # We need to generate a drawable for each behavior
        for behavior in config["behaviors"]:
            behaviorId = to_behavior_id(config, behavior["id"])
            print(F'    <bitmap id="{behaviorId}" filename="icon_{behaviorId}.png" />', file=out_file)

        print(F"</drawables>", file=out_file)




 #####                                      
#     # ##### #####  # #    #  ####   ####  
#         #   #    # # ##   # #    # #      
 #####    #   #    # # # #  # #       ####  
      #   #   #####  # #  # # #  ###      # 
#     #   #   #   #  # #   ## #    # #    # 
 #####    #   #    # # #    #  ####   ####  

def assemble_languages(config):
    """Assembles all language codes used in the given config."""

    # We always want English
    language_codes = { "en" }

    for drawable in config["drawables"]:
        for language_code in drawable["languages"]:
            language_codes.add(language_code)

    for behavior in config["behaviors"]:
        for language_code in behavior["languages"]:
            language_codes.add(language_code)
    
    return language_codes


def generate_string(item, item_id, language_code, out_file):
    # Check if this item has a translation
    if not language_code in item["languages"]:
        print(F"{item_id} has no translation for {language_code}")
    else:
        print(F'    <string id="{item_id}">{item["languages"][language_code]}</string>', file=out_file)



def generate_strings(config):
    """Generates language definitions for the given config."""

    for language_code in assemble_languages(config):
        dir_name = "resources"
        if language_code != "en":
            dir_name += F"-{language_code}"
        
        with open(F"{dir_name}/strings/strings{to_file_name_suffix(config)}.xml", mode="w", encoding="utf8", newline="\n") as out_file:
            print(F"<!-- {GENERATED_FILE_WARNING} -->", file=out_file)
            print("<strings>", file=out_file)

            # We need to generate a string for each drawable
            print("    <!-- Drawables -->", file=out_file)
            for drawable in config["drawables"]:
                drawableId = to_drawable_id(config, drawable["id"])
                generate_string(drawable, drawableId, language_code, out_file)

            print("", file=out_file)
            print("    <!-- Behaviors -->", file=out_file)
            for behavior in config["behaviors"]:
                behaviorId = to_behavior_id(config, behavior["id"])
                generate_string(behavior, behaviorId, language_code, out_file)

            print("</strings>", file=out_file)




#     #                             
##   ## ###### #    # #    #  ####  
# # # # #      ##   # #    # #      
#  #  # #####  # #  # #    #  ####  
#     # #      #  # # #    #      # 
#     # #      #   ## #    # #    # 
#     # ###### #    #  ####   ####  

def generate_menus(config):
    """Generates a selection menu for the available behaviors, sorted by English name."""

    with open(F"resources/menu/settingsMenu{config['category']}Selection.xml", mode="w", encoding="utf8", newline="\n") as out_file:
        print(F"<!-- {GENERATED_FILE_WARNING} -->", file=out_file)
        print(F'<menu2 id="SettingsMenu{config["category"]}Selection" title="@Strings.{config["category"]}">', file=out_file)

        for behavior in sorted_by_localized_name(config["behaviors"]):
            behavior_id = to_behavior_id(config, behavior["id"])
            print(F'    <icon-menu-item id="{behavior_id}" label="@Strings.{behavior_id}" icon="@Drawables.{behavior_id}" />', file=out_file)

        print(F'</menu2>', file=out_file)


        

#     #                     #####                               
##   ##   ##   # #    #    #     #  ####  #####  # #####  ##### 
# # # #  #  #  # ##   #    #       #    # #    # # #    #   #   
#  #  # #    # # # #  #     #####  #      #    # # #    #   #   
#     # ###### # #  # #          # #      #####  # #####    #   
#     # #    # # #   ##    #     # #    # #   #  # #        #   
#     # #    # # #    #     #####   ####  #    # # #        #   

# Our configuration files
config_files = [ "indicators", "meters" ]

for file in config_files:
    with open(F"source/{file}.json") as json_file:
        config = json.load(json_file)

        # We will probably shuffle lists around, so remember the original order
        add_index_field(config["drawables"])
        add_index_field(config["behaviors"])

        # Generate all the code we need
        generate_drawables(config)
        generate_strings(config)
        generate_menus(config)
