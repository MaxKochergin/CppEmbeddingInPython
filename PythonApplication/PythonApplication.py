#https://dearpygui.readthedocs.io/en/latest/documentation/node-editor.html
import dearpygui.dearpygui as dpg
import PybindEmbedding as pe

global NodesList
NodesList = []
global compLinks
compLinks = []
global ComponentListNodes
ComponentListNodes = []


class ComponentThumb:
    #counter of components
    count = -1
    def __init__(self, name, inVar, outVar):
        ComponentThumb.count += 1
        ComponentListNodes.append([])#добавляем компонент=список в список
        #print(f'{ComponentThumb.count=}')
        self.component = pe.Component(name, inVar, outVar)
        with dpg.node(label = name, tag = 'node' + str(ComponentThumb.count)) as self.thumb:
            #входной узел слева
            NodesList.append(len(NodesList))
            with dpg.node_attribute(label="Node A1", tag=len(NodesList)) as self.node1:
                dpg.add_input_float(label="inVar", width=150)
                #dpg.add_input_text(label="str", width=150)
            ComponentListNodes[ComponentThumb.count].append(len(NodesList))#добавляем узел
            #выходной узел справа
            NodesList.append(len(NodesList))
            with dpg.node_attribute(label="Node A2", attribute_type=dpg.mvNode_Attr_Output,tag=len(NodesList)):
                dpg.add_input_float(label="outVar", width=150)
            ComponentListNodes[ComponentThumb.count].append(len(NodesList))



# Creating context
dpg.create_context()

# Allow Cyrillic in window
big_let_start = 0x00C0  # Capital "A" in cyrillic alphabet
big_let_end = 0x00DF  # Capital "Я" in cyrillic alphabet
small_let_end = 0x00FF  # small "я" in cyrillic alphabet
remap_big_let = 0x0410  # Starting number for remapped cyrillic alphabet
alph_len = big_let_end - big_let_start + 1  # adds the shift from big letters to small
alph_shift = remap_big_let - big_let_start  # adds the shift from remapped to non-remapped

with dpg.font_registry():
    with dpg.font("C:/Windows/Fonts/times.ttf", 20) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        biglet = remap_big_let  # Starting number for remapped cyrillic alphabet
        for i1 in range(big_let_start, big_let_end + 1):  # Cycle through big letters in cyrillic alphabet
            dpg.add_char_remap(i1, biglet)  # Remap the big cyrillic letter
            dpg.add_char_remap(i1 + alph_len, biglet + alph_len)  # Remap the small cyrillic letter
            biglet += 1  # choose next letter

# callback runs when user attempts to connect attributes
def link_callback(sender, app_data):
    # app_data -> (link_id1, link_id2)
    link = dpg.add_node_link(app_data[0], app_data[1], parent=sender, tag = 101)
    print(app_data[0], ' connected to ', app_data[1], ': sender', sender)
    compLinks.append([app_data[0], app_data[1]])
    print(f'{compLinks=}')
    #dpg.bind_item_handler_registry(101,'widget handler')


# callback runs when user attempts to disconnect attributes
def delink_callback(sender, app_data):
    # app_data -> link_id
    dpg.delete_item(app_data)

def ModelRun(sender, app_data, user_data):
    #print('Button was pressed')
    #if user_data is list:
    #    user_data[0].SendMessagePy(user_data[1],0)
    #    print('Component 2 received message: ', f'{user_data[1].outputDouble=}')
    #else:
    #    raise TypeError('ModelRun: curcuit is not a list')
    print('Button was pressed')
    user_data[0].component.SendMessage(user_data[1].component,0)
    print('Component 2 received message: ', f'{user_data[1].component.outputDouble=}')

with dpg.window(label="Testing DearPyGUI with Pybind11", width=400, height=400):
    dpg.bind_font(default_font)
    with dpg.menu_bar():

            with dpg.menu(label="Menu"):
                dpg.add_menu_item(label="Run model", callback=ModelRun)
    with dpg.node_editor(callback=link_callback, delink_callback=delink_callback) as nodeEditorID:
        print('dpg.node_editor is ', nodeEditorID)
        curcuit = []
        curcuit.append(ComponentThumb('Component 1',0.0,1.0))
        curcuit.append(ComponentThumb('Component 2',0.0,0.0))
        print(f'{curcuit=}', f'{len(curcuit)=}')
        print(f'{NodesList=}')
        print(f'{compLinks=}')
        print(f'{ComponentListNodes=}')
with dpg.window():
    dpg.add_button(label='ModelRun', callback=ModelRun,user_data = curcuit)
        ##with dpg.collapsing_header(label="Widgets"):
    ##    with dpg.group(horizontal=True):
    ##        dpg.add_button(label="Click", callback=ModelRun)
        #with dpg.node(label="Node 1"):
        #    with dpg.node_attribute(label="Node A1"):
        #        dpg.add_input_float(label="F1", width=150)

        #    with dpg.node_attribute(label="Node A2", attribute_type=dpg.mvNode_Attr_Output):
        #        dpg.add_input_float(label="F2", width=150)

        #with dpg.node(label="Node 2"):
        #    with dpg.node_attribute(label="Node A3"):
        #        dpg.add_input_float(label="F3", width=200)

        #    with dpg.node_attribute(label="Node A4", attribute_type=dpg.mvNode_Attr_Output):
        #        dpg.add_input_float(label="F4", width=200)
    
# Creating Viewport (window created by the operating system)
dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
# Destroying context
dpg.destroy_context()