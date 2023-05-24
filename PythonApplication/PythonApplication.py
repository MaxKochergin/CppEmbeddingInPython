#https://dearpygui.readthedocs.io/en/latest/documentation/node-editor.html
import dearpygui.dearpygui as dpg
import PybindEmbedding as pe

class ComponentThumb:
    def __init__(self, name, inVar, outVar):
        self.component = pe.Component(name, inVar, outVar)
        with dpg.node(label=name):
           with dpg.node_attribute(label="Node A1"):
                dpg.add_input_float(label="inVar", width=150)

           with dpg.node_attribute(label="Node A2", attribute_type=dpg.mvNode_Attr_Output):
                dpg.add_input_float(label="outVar", width=150)



dpg.create_context()

# callback runs when user attempts to connect attributes
def link_callback(sender, app_data):
    # app_data -> (link_id1, link_id2)
    dpg.add_node_link(app_data[0], app_data[1], parent=sender)

# callback runs when user attempts to disconnect attributes
def delink_callback(sender, app_data):
    # app_data -> link_id
    dpg.delete_item(app_data)

def ModelRun():
    print('Button was pressed')

with dpg.window(label="Testing DearPyGUI with Pybind11", width=400, height=400):
    with dpg.menu_bar():

            with dpg.menu(label="Menu"):
                dpg.add_menu_item(label="Run model", callback=ModelRun)
    with dpg.node_editor(callback=link_callback, delink_callback=delink_callback):
        curcuit = []
        curcuit.append(ComponentThumb('Component 1',0.0,1.0))
        curcuit.append(ComponentThumb('Component 2',0.0,0.0))
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

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()