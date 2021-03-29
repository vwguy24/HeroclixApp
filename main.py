from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition, SlideTransition
# from screen_helper import screen_helper
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from Get_Card import ff_TMNT4, TMNT4_, ff_BTAS, BTAS_, ff_EAX, EAX_, ff_SWB, SWB_, ff_RE, RE_, ABPI_, CMM_, ff_ABPI, WCR_, trek_RF, ff_TNG, XDPS_, ff_XDPS, trek_BG, ORVL_, WWE_, dc_XM, CAAV_, ff_CAAV, JLU_, BWM_, FFCC_, bg_AME, ff_F4, F4_, ff_SVC, SVC_, HX_, ff_HX, dc_FF, FFFF_, ff_FFFF, PAC_Sheet
from kivy.uix.popup import Popup
from kivy.factory import Factory as F
from kivy.core.window import Window
# Sets screen to mobile phone size delete before use
# Window.size = (300, 500)
Heroclix = "None"

ImageKey = "None"
# Set all screens first so we can build them later
# Build screens that look similar and all come back to home screen
# Has a list that uses outside functions to fill with figure names
screen_helper = """
<MyTile@SmartTileWithLabel>
    size_hint_y: None
    height: "240dp"
    
ScreenManager:
    DummyScreen:
    MenuScreen:
    FF_TMNT4:
    TMNT4:
    FF_BTAS:
    BTAS:
    SWB:
    FF_SWB:
    FF_EAX:
    EAX:
    CMM:
    RE:
    FF_RE:
    ABPI:
    FF_ABPI:
    WCR:
    TREK_RF:
    FF_TNG:
    XDPS:
    FF_XDPS:
    TREK_BG:
    ORVL:
    WWE:
    DC_XM:
    CAAV:
    FF_CAAV:
    JLU:
    BWM:
    FFCC:
    BG_AME:
    FF_F4:
    F4:
    FF_SVC:
    SVC:
    HX:
    FF_HX:
    DC_FF:
    FFFF:
    FF_FFFF:
    Rules:
    Powers:

    

<DummyScreen>
    name: 'dummy'

<MenuScreen>:
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Home'
            elevation: 8
            
        Spinner: 
            id: whatever
            text: "-Set-"
            values: ["FF_TMNT4", "TMNT4","BTAS","FF_BTAS", "SWB", "FF_SWB", "EAX", "FF_EAX", "CMM", "RE", "FF_RE", "ABPI", "FF_ABPI", "WCR", "TREK_RF", "FF_TNG", "XDPS", "FF_XDPS", "TREK_BG", "ORVL", "WWE", "DC_XM", "CAAV", "FF_CAAV", "JLU", "BWM", "FFCC", "BG_AME", "FF_F4", "F4", "FF_SVC", "SVC", "HX", "FF_HX", "DC_FF", "FFFF", "FF_FFFF"]
            on_text:
                root.on_spinner_select(self.text)
            
                
        MDGridLayout:
            cols: 2
            adaptive_height: True
            padding: dp(4), dp(4)
            spacing: dp(4)
            
            MDRectangleFlatButton:
                text: 'Powers'
                on_press: root.manager.current = 'powers'
            MDRectangleFlatButton:
                text: 'Rules'
                on_press: root.manager.current = 'rules'
            
        MDBottomAppBar:
            MDToolbar:
                # title: 'help'
                # left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'

<FF_TMNT4>:
    name: 'FF_TMNT4'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: ff_tmnt4
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'

<TMNT4>:
    name: 'TMNT4'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: tmnt4
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'

<FF_BTAS>:
    name: 'FF_BTAS'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: ff_btas
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'

<BTAS>:
    name: 'BTAS'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: btas
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'

<FF_SWB>:
    name: 'FF_SWB'
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            MDGridLayout:
                id: ff_swb
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'

<SWB>:
    name: 'SWB'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: swb
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'

<FF_EAX>:
    name: 'FF_EAX'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: ff_eax
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'

<CMM>:
    name: 'CMM'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: cmm
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'

<RE>:
    name: 'RE'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: re
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'

<FF_RE>:
    name: 'FF_RE'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: ff_re
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'

<ABPI>:
    name: 'ABPI'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: abpi
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
<FF_ABPI>:
    name: 'FF_ABPI'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: ff-abpi
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
<WCR>:
    name: 'WCR'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: wcr
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
<TREK_RF>:
    name: 'TREK_RF'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: trek_rf
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<FF_TNG>:
    name: 'FF_TNG'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: ff_tng
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
<XDPS>:
    name: 'XDPS'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: xdps
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
<TREK_BG>:
    name: 'TREK_BG'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: trek_bg
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<ORVL>:
    name: 'ORVL'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: orvl
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<WWE>:
    name: 'WWE'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: wwe
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<DC_XM>:
    name: 'DC_XM'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: dc_xm
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<CAAV>:
    name: 'CAAV'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: caav
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<FF_CAAV>:
    name: 'FF_CAAV'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: ff_caav
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<JLU>:
    name: 'JLU'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: jlu
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<BWM>:
    name: 'BWM'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: bmw
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<FFCC>:
    name: 'FFCC'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: ffcc
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<BG_AME>:
    name: 'BG_AME'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: bg_ame
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<FF_F4>:
    name: 'FF_F4'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: ff_f4
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<F4>:
    name: 'F4'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: f4
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<FF_SVC>:
    name: 'FF_SVC'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: ff_svc
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<SVC>:
    name: 'SVC'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: svc
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<HX>:
    name: 'HX'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: hx
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<FF_HX>:
    name: 'FF_HX'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: ff_hx
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<DC_FF>:
    name: 'DC_FF'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: dc_ff
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<FFFF>:
    name: 'FFFF'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: ffff
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                
                
                
<FF_FFFF>:
    name: 'FF_FFFF'
    BoxLayout:
        orientation: 'vertical'
        ScrollView: 
            MDGridLayout:
                id: ff_ffff
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'
                


<Powers>:
    name: 'powers'
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
        
            MDGridLayout:
                id: powers
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
                
                
        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'

                
<Rules>:
    name: 'rules'
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
    
            MDGridLayout:
                cols: 2
                adaptive_height: True
                padding: dp(4), dp(4)
                spacing: dp(4)
        
                MyTile:
                    source: 'Rules_1.JPG'
        
                MyTile:
                    source: 'Rules_2.JPG'
        
                MyTile:
                    source: 'Rules_3.JPG'
    
                MyTile:
                    source: 'Rules_4.JPG'
        
                MyTile:
                    source: 'Rules_5.JPG'
        
                MyTile:
                    source: 'Rules_6.JPG'
    
                MyTile:
                    source: 'Rules_7.JPG'
        
                MyTile:
                    source: 'Rules_8.JPG'
        
                MyTile:
                    source: 'Rules_9.JPG'
        
                MyTile:
                    source: 'Rules_10.JPG'
        
                MyTile:
                    source: 'Rules_11.JPG'
    
                MyTile:
                    source: 'Rules_12.JPG'
        
                MyTile:
                    source: 'Rules_13.JPG'
        
                MyTile:
                    source: 'Rules_14.JPG'
    
                MyTile:
                    source: 'Rules_15.JPG'
        
                MyTile:
                    source: 'Rules_16.JPG'
    
                MyTile:
                    source: 'Rules_17.JPG'
        
                MyTile:
                    source: 'Rules_18.JPG'
        
                MyTile:
                    source: 'Rules_19.JPG'
    
                MyTile:
                    source: 'Rules_20.JPG'
        
                MyTile:
                    source: 'Rules_21.JPG'
        
                MyTile:
                    source: 'Rules_22.JPG'
    
                MyTile:
                    source: 'Rules_23.JPG'
        
                MyTile:
                    source: 'Rules_24.JPG'


        MDBottomAppBar:
            MDToolbar:
                title: 'help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: "free-end"
                type: 'bottom'
                icon: 'home'
                on_action_button: root.manager.current = 'menu'


"""

# Set up function to delay and let everything load this was to use outside python files (Get_Card.py)
class DummyScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.switch_screen)

    def switch_screen(self, dt):
        self.manager.transition = NoTransition()
        self.manager.current = "menu"
        self.manager.transition = SlideTransition()

# Menu class function
class MenuScreen(Screen):
    # Set up function that changes page
    def on_spinner_select(self, choice):
        self.manager.current = choice


# ff TMNT4 page that matches up with page in builder as it has same name as the class
class FF_TMNT4(Screen):
    # Set up Open_ff_TMNT4() function to pop up picture
    # def Open_ff_TMNT4(self, pic):
    # Select image from dictionary and displays image
    # source = FF_TMNT4[pic]

    # Load this as the page loads
    def on_pre_enter(self):
        # Go through ff TMNT4 dictionary from Get_Card.py and list each key in list
        for key in ff_TMNT4:
            self.ids.ff_tmnt4.add_widget(F.MyTile(source = ff_TMNT4[key], text = key))
        # for key in FF_TMNT4:
            # Have print to test to make sure it went through
            # print(key)
            # Set icon to android for now can change later to something that fits better
            # icon = IconLeftWidget(icon='android')
            # Set type of line
            # items = OneLineIconListItem(text=key)
            # Adds the icon to the list item
            # items.add_widget(icon)
            # Adds the item to list in builder to print out
            # self.ids.ff_tmnt4.add_widget(items)

# Functions for the TMNT4 screen
class TMNT4(Screen):
    # Set to do before screen loads
    def on_pre_enter(self):
        # Goes through the dictionary named TMNT4 from Get_Card.py
        for key in TMNT4_:
            self.ids.tmnt4.add_widget(F.MyTile(source = TMNT4_[key], text = key))
        # for key in TMNT4:
            # Copied from first function was just for testing
            # print(key)
            # Set icon to android for now (can change later to something that fits better)
            # icon = IconLeftWidget(icon='android')
            # Set text of line item and line item type
            # items = OneLineIconListItem(text=key)
            # Add icon to items widget
            # items.add_widget(icon)
            # Add item to list in screen builder
            # self.ids.tmnt4.add_widget(items)

# Class that connects to ff BTAS page in screen builder
class FF_BTAS(Screen):
    # Do this function before screen loads
    def on_pre_enter(self):
        # Move through the FF_BTAS dictionary
        for key in ff_BTAS:
            self.ids.ff_btas.add_widget(F.MyTile(source = FF_BTAS[key], text = key))
        # for key in FF_BTAS:
            # Copied from first one just a test
            # print(key)
            # Set icon to android can be changed later when we find something that fits better
            # icon = IconLeftWidget(icon='android')
            # Set type of list item and set text of item to key value in dictionary
            # items = OneLineIconListItem(text=key)
            # Add icon to the list item
            # items.add_widget(icon)
            # Load items into list this corresponds with
            # self.ids.ff_btas.add_widget(items)

# Set up functions that connect to the respective screen in screen builder
class BTAS(Screen):
    # Do this before loading the page
    def on_pre_enter(self):
        # Go through the dictionary from Get_Card.py
        for key in BTAS_:
            self.ids.btas.add_widget(F.MyTile(source = BTAS_[key], text = key))
        # for key in BTAS:
            # Copied from others just a test
            # print(key)
            # Set icon can be changed later
            # icon = IconLeftWidget(icon='android')
            # Set list item up and set text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add item to list in screen builder
            # self.ids.btas.add_widget(items)

# Set up functions that connect to respective screen
class SWB(Screen):
    # Do this before screen loads
    def on_pre_enter(self):
        # Go through respective dictionary
        for key in SWB_:
            self.ids.swb.add_widget(F.MyTile(source = SWB_[key], text = key))
        # for key in SWB:
            # Copied just a test
            # print(key)
            # Set up icon can be changed when something better is found
            # icon = IconLeftWidget(icon='android')
            # Set type of list item and text value to key
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add items to list in builder screen
            # self.ids.swb.add_widget(items)

# Set up functions for respective screen
class FF_SWB(Screen):
    # Do this befor screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in ff_SWB:
            self.ids.ff_swb.add_widget(F.MyTile(source = ff_SWB[key], text = key))
        # for key in FF_SWB:
            # Copied just a test
            # print(key)
            # Set icon until better one decided
            # icon = IconLeftWidget(icon='android')
            # Set type of list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to item
            # items.add_widget(icon)
            # Add items to list in respective screen
            # self.ids.ff_swb.add_widget(items)

# Set up functions that work with respective screen
class FF_EAX(Screen):
    # Do this before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in ff_EAX:
            self.ids.ff_eax.add_widget(F.MyTile(source = ff_EAX[key], text = key))
        # for key in FF_EAX:
            # Copied just a test
            # print(key)
            # Set icon can change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Put list items on respective screen
            # self.ids.ff_eax.add_widget(items)

# Set up functions for respective screen
class EAX(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in EAX_:
            self.ids.eax.add_widget(F.MyTile(source = EAX_[key], text = key))
        # for key in EAX:
            # Copied just a test
            # print(key)
            # Set icon will be changed later
            # icon = IconLeftWidget(icon='android')
            # Set type of item list
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add item to list of respective screen
            # self.ids.eax.add_widget(items)


# Set up functions for respective screen
class CMM(Screen):
    # Do this before loading screen
    def on_pre_enter(self):
        # Move through dictionary
        for key in CMM_:
            self.ids.cmm.add_widget(F.MyTile(source = CMM_[key], text = key))
        # for key in CMM:
            # Copied just a test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set list item type and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to respective screen
            # self.ids.cmm.add_widget(items)

# Set up functions for respective screen
class RE(Screen):
    # Do this before loading page
    def on_pre_enter(self):
        # Move through dictionary
        for key in RE_:
            self.ids.re.add_widget(F.MyTile(source = RE_[key], text = key))
        # for key in RE:
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set type of list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            # self.ids.re.add_widget(items)

# Set up functions for respective screen
class FF_RE(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in ff_RE:
            self.ids.ff_re.add_widget(F.MyTile(source = ff_RE[key], text = key))
        # for key in FF_RE:
            # Copied just test
            # print(key)
            # Set up icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item type and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list items to list of respective screen
            # self.ids.ff_re.add_widget(items)

# Set up functions for respective screen
class ABPI(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in ABPI_:
            self.ids.abpi.add_widget(F.MyTile(source = ABPI_[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class FF_ABPI(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in ff_ABPI:
            self.ids.ff_abpi.add_widget(F.MyTile(source = ff_ABPI[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class WCR(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in WCR_:
            self.ids.wcr.add_widget(F.MyTile(source = WCR_[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class TREK_RF(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in trek_RF:
            self.ids.trek_rf.add_widget(F.MyTile(source = trek_RF[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class FF_TNG(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in ff_TNG:
            self.ids.ff_tng.add_widget(F.MyTile(source = ff_TNG[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class XDPS(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in XDPS_:
            self.ids.xdps.add_widget(F.MyTile(source = XDPS_[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class FF_XDPS(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in ff_XDPS:
            self.ids.ff_xdps.add_widget(F.MyTile(source = ff_XDPS[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class TREK_BG(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in trek_BG:
            self.ids.trek_bg.add_widget(F.MyTile(source = trek_BG[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class ORVL(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in ORVL_:
            self.ids.orvl.add_widget(F.MyTile(source = ORVL_[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class WWE(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in WWE_:
            self.ids.wwe.add_widget(F.MyTile(source = WWE_[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class DC_XM(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in dc_XM:
            self.ids.dc_xm.add_widget(F.MyTile(source = dc_XM[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class CAAV(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in CAAV_:
            self.ids.caav.add_widget(F.MyTile(source = CAAV_[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class FF_CAAV(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in ff_CAAV:
            self.ids.ff_caav.add_widget(F.MyTile(source = ff_CAAV[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class JLU(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in JLU_:
            self.ids.jlu.add_widget(F.MyTile(source = JLU_[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class BWM(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in BWM_:
            self.ids.bwm.add_widget(F.MyTile(source = BWM_[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class FFCC(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in FFCC_:
            self.ids.ffcc.add_widget(F.MyTile(source = FFCC_[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class BG_AME(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in bg_AME:
            self.ids.bg_ame.add_widget(F.MyTile(source = bg_AME[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class FF_F4(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in ff_F4:
            self.ids.ff_f4.add_widget(F.MyTile(source = ff_F4[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class F4(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in F4_:
            self.ids.f4.add_widget(F.MyTile(source = F4_[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class FF_SVC(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in ff_SVC:
            self.ids.ff_svc.add_widget(F.MyTile(source = ff_SVC[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class SVC(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in SVC_:
            self.ids.svc.add_widget(F.MyTile(source = SVC_[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class HX(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in HX_:
            self.ids.hx.add_widget(F.MyTile(source = HX_[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class FF_HX(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in ff_HX:
            self.ids.ff_hx.add_widget(F.MyTile(source = ff_HX[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class DC_FF(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in dc_FF:
            self.ids.dc_ff.add_widget(F.MyTile(source = dc_FF[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class FFFF(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in FFFF_:
            self.ids.ffff.add_widget(F.MyTile(source = FFFF_[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)


# Set up functions for respective screen
class FF_FFFF(Screen):
    # Do before screen loads
    def on_pre_enter(self):
        # Move through dictionary
        for key in ff_FFFF:
            self.ids.ff_ffff.add_widget(F.MyTile(source = ff_FFFF[key], text = key))
            # Copied just test
            # print(key)
            # Set icon change later
            # icon = IconLeftWidget(icon='android')
            # Set up list item and text value
            # items = OneLineIconListItem(text=key)
            # Add icon to list item
            # items.add_widget(icon)
            # Add list item to list of respective screen
            #self.ids.abpi.add_widget(items)

# Set up functions for rules
class Rules(Screen):
    # Load pictures to tiles on enter
    def on_pre_enter(self):
        # Read list of pictures and put on tiles
        print("placeholder")

# Set up functions for powers
class Powers(Screen):
    # Load pictures to tiles on enter
    def on_pre_enter(self):
        # Read list of pictures and put on tiles
        for i in PAC_Sheet:
            self.ids.powers.add_widget(F.MyTile(source = i))

        print("placeholder")



# Popup class to set to picture of figure
class P(FloatLayout):
    pass

# Define functions for each page's popup (need to go through right dictionary)\
def Show_ff_TMNT4():
    show = P()



# Set up functions for respective screen
class UploadScreen(Screen):

    pass

# Set up screen manager to hold all screens
sm = ScreenManager()
# Connect each string to its respective functions
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(FF_TMNT4(name='ff_tmnt4'))
sm.add_widget(TMNT4(name='tmnt4'))
sm.add_widget(FF_BTAS(name='ff_btas'))
sm.add_widget(BTAS(name='btas'))
sm.add_widget(SWB(name='swb'))
sm.add_widget(FF_SWB(name='ff_swb'))
sm.add_widget(FF_EAX(name='ff_eax'))
sm.add_widget(EAX(name='eax'))
sm.add_widget(CMM(name='cmm'))
sm.add_widget(RE(name='re'))
sm.add_widget(FF_RE(name='ff_re'))
sm.add_widget(ABPI(name='abpi'))
sm.add_widget(FF_ABPI(name='ff_abpi'))
sm.add_widget(WCR(name='wcr'))
sm.add_widget(TREK_RF(name='trek_rf'))
sm.add_widget(FF_TNG(name='ff_tng'))
sm.add_widget(XDPS(name='xdps'))
sm.add_widget(FF_XDPS(name='ff_xdps'))
sm.add_widget(TREK_BG(name='trek_bg'))
sm.add_widget(ORVL(name='orvl'))
sm.add_widget(WWE(name='wwe'))
sm.add_widget(DC_XM(name='dc_xm'))
sm.add_widget(CAAV(name='caav'))
sm.add_widget(FF_CAAV(name='ff_caav'))
sm.add_widget(JLU(name='jlu'))
sm.add_widget(BWM(name='bwm'))
sm.add_widget(FFCC(name='ffcc'))
sm.add_widget(BG_AME(name='bg_ame'))
sm.add_widget(FF_F4(name='ff_f4'))
sm.add_widget(F4(name='f4'))
sm.add_widget(FF_SVC(name='ff_svc'))
sm.add_widget(SVC(name='svc'))
sm.add_widget(HX(name='hx'))
sm.add_widget(FF_HX(name='ff_hx'))
sm.add_widget(DC_FF(name='dc_ff'))
sm.add_widget(FFFF(name='ffff'))
sm.add_widget(FF_FFFF(name='ff_ffff'))
sm.add_widget(DummyScreen(name='dummy'))
sm.add_widget(Rules(name='rules'))
sm.add_widget(Powers(name = 'powers'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    def On_click(self):
        global Heroclix
        print(Heroclix)


DemoApp().run()


# After making tiles for powers and abilities sheet, could make lists into pictures of the figures