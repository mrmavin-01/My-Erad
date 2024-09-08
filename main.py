from urllib import request
from kivy.network.urlrequest import UrlRequest
from kivy.clock import Clock
from kivy.uix.carousel import Carousel
from kivymd.uix.button import MDFillRoundFlatButton
#from kivy.uix.image import Image
from kivy.lang import Builder
from kivymd.uix.bottomsheet import MDBottomSheet
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDFlatButton
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from kivy.utils import platform
from kivy.clock import mainthread
from jnius import autoclass
from plyer import vibrator
from kivy.core.audio import SoundLoader


kv = '''
MDScreenManager:
	
#Login page
    MDScreen:
		name :"log in"
		MDBoxLayout:
			orientation:"vertical"
			spacing: "20dp"	
		
			MDTopAppBar:
				id:"heading"
				md_bg_color:"white"
				#title:"Welcome"
				MDLabel:
				    text:"Login Page"
		    		halign:"center"
	    			bold : True

			MDLabel:
				text:"Welcome to ERAD App enter your username and password for your increasing security"
				halign:"center"
				bold : True


            MDCard:
                orientation: 'vertical'
                style: "elevated"
                size_hint: None, None
                size: "280dp", "240dp"
                pos_hint: {"center_x": .5, "center_y": .5}
                MDLabel:
                    text: "LOGIN"
                    halign: "center"
                    theme_text_color: "Secondary"
                    font_style: "H4"
                    bold: True
                
	    		MDTextField:
		    		id:name
		    		text:""
			    	mode:"line"
		    		pos_hint: {'center_x': .5, 'center_y': .5}
    				size_hint_x: None
    				width: "200dp"
    				hint_text: "Name"
    				required: True
    				
                MDTextField:
                	id:password
                	text:""
			    	mode:"line"
			    	pos_hint: {'center_x': .5, 'center_y': .5}
		    		size_hint_x: None
                    width: "200dp"
                    hint_text: "Password"
                    required: True
                    
            MDTextButton:
            	text:"Login"
            	pos_hint: {'center_x': .5}
            	color:"green"
            	on_release:app.home()
            MDTextButton:
            	id:button
            	text:" "
            	pos_hint: {'center_x': .5, 'center_y': .5}
            	color:"red"
            		
            Widget:
            Widget:
			
# Home screen
    MDScreen:
        name: "home"
        MDBoxLayout:
            orientation: "vertical"
            spacing: "4dp"
            MDTopAppBar:
                id: "heading"
                md_bg_color: "black"
                title: "Welcome"
            ScrollView:
                orientation:"vertical"
                bar_width: 4
                MDList:
                    id: scroll_list
                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: "12dp"
                        padding: "12dp"
                        size_hint_y: None
                        height: self.minimum_height #force height calculation 

                    
                    MDLabel:
                        text:"      Personal Information"
                        bold: True
                        pos_hint: {'center_x':  .5}
                    MDSeparator:
                        height: "1dp"
                        
                        MDGridLayout:
                            cols: 1
                            padding: "10dp"
                            spacing: "10dp"
                            
                            MDCard:  # Button 1
                                orientation: "vertical"
                                padding: "10dp"
                                elevation: 1
                                size_hint_y: None 
                                height: "80dp"
                                ripple_behavior: True 
                                on_release: app.profile()
                                # Add your button action here
                                MDBoxLayout:  # Horizontal layout for image and label
                                    orientation: "horizontal"
                                    spacing: "10dp"  # Adjust spacing as needed
                                    Image:
                                        source: "/storage/emulated/0/python_app/profile.png"
                                        allow_stretch: True
                                        keep_ratio: True
                                        size_hint: (None, None)
                                        size: ("60dp", "70dp")
                                    MDLabel:
                                        text: "My Profile"
                                        font_style: "H6"
                                        halign: "left" 
                                        valign: "center"
                                    
                            MDCard:  # Button 1
                                orientation: "vertical"
                                padding: "10dp"
                                elevation: 1
                                size_hint_y: None 
                                height: "80dp"
                                ripple_behavior: True 
                                on_release: print("Button 1 pressed!")  # Add your button action here
                                MDBoxLayout:  # Horizontal layout for image and label
                                    orientation: "horizontal"
                                    spacing: "4dp"  # Adjust spacing as needed
                                    Image:
                                        source: "/storage/emulated/0/python_app/5690898.png"
                                        allow_stretch: True
                                        keep_ratio: True
                                        size_hint: (None, None)
                                        size: ("60dp", "70dp")
                                    MDLabel:
                                        text: "Log out"
                                        font_style: "H6"
                                        halign: "left" 
                                        valign: "center"
                                    
                            MDBoxLayout:
                                orientation: "horizontal"
                                spacing: "4dp"
                                padding: "12dp"
                                    
                            MDLabel:
                                text:"      Cash Details."
                                bold: True
                                pos_hint: {'center_x':  .5}
                                
                            MDSeparator:
                                height: "1dp"
                             
                            MDCard:  # Button 1
                                orientation: "vertical"
                                padding: "10dp"
                                elevation: 1
                                size_hint_y: None 
                                height: "80dp"
                                ripple_behavior: True 
                                on_release: app.earning() # Add your button action here
                                MDBoxLayout:  # Horizontal layout for image and label
                                    orientation: "horizontal"
                                    spacing: "4dp"  # Adjust spacing as needed
                                    Image:
                                        source: "/storage/emulated/0/python_app/earnings.png"
                                        allow_stretch: True
                                        keep_ratio: True
                                        size_hint: (None, None)
                                        size: ("60dp", "70dp")
                                    MDLabel:
                                        text: "Earning Chamber"
                                        font_style: "H6"
                                        halign: "left" 
                                        valign: "center"
                                    
                            MDCard:  # Button 1
                                orientation: "vertical"
                                padding: "10dp"
                                elevation: 1
                                size_hint_y: None 
                                height: "80dp"
                                ripple_behavior: True 
                                on_release: print("Button 1 pressed!")  # Add your button action here
                                MDBoxLayout:  # Horizontal layout for image and label
                                    orientation: "horizontal"
                                    spacing: "4dp"  # Adjust spacing as needed
                                    Image:
                                        source: "/storage/emulated/0/python_app/law.png"
                                        allow_stretch: True
                                        keep_ratio: True
                                        size_hint: (None, None)
                                        size: ("60dp", "70dp")
                                    MDLabel:
                                        text: "Balance"
                                        font_style: "H6"
                                        halign: "left" 
                                        valign: "center"
                                    
                            MDBoxLayout:
                                spacing: "4dp"
                                padding: "12dp"
                                    
                            MDLabel:
                                text:"      General Settings"
                                bold: True
                                pos_hint: {'center_x':  .5}
                                
                            MDSeparator:
                                height: "1dp"
                             
                            MDCard:  # Button 1
                                orientation: "vertical"
                                padding: "10dp"
                                elevation: 1
                                size_hint_y: None 
                                height: "80dp"
                                ripple_behavior: True 
                                on_release: print("Button 1 pressed!")  # Add your button action here
                                MDBoxLayout:  # Horizontal layout for image and label
                                    orientation: "horizontal"
                                    spacing: "4dp"  # Adjust spacing as needed
                                    Image:
                                        source: "/storage/emulated/0/python_app/cogwheel.png"
                                        allow_stretch: True
                                        keep_ratio: True
                                        size_hint: (None, None)
                                        size: ("60dp", "60dp")
                                    MDLabel:
                                        text: "Setting"
                                        font_style: "H6"
                                        halign: "left" 
                                        valign: "center"
                                    
                            MDCard:  # Button 1
                                orientation: "vertical"
                                padding: "10dp"
                                elevation: 1
                                size_hint_y: None 
                                height: "80dp"
                                ripple_behavior: True 
                                on_release: print("Button 1 pressed!")  # Add your button action here
                                MDBoxLayout:  # Horizontal layout for image and label
                                    orientation: "horizontal"
                                    spacing: "4dp"  # Adjust spacing as needed
                                    Image:
                                        source: "/storage/emulated/0/python_app/question.png"
                                        allow_stretch: True
                                        keep_ratio: True
                                        size_hint: (None, None)
                                        size: ("60dp", "70dp")
                                    MDLabel:
                                        text: "Help"
                                        font_style: "H6"
                                        halign: "left" 
                                        valign: "center"
                            
                            MDBoxLayout:
                                spacing: "4dp"
                                padding: "12dp"
                                    
                            MDLabel:
                                text:"      Our Offer"
                                bold: True
                                pos_hint: {'center_x':  .5}
                                
                            MDSeparator:
                                height: "1dp"
                             
                            MDCard:  # Button 1
                                orientation: "vertical"
                                padding: "10dp"
                                elevation: 1
                                size_hint_y: None 
                                height: "80dp"
                                ripple_behavior: True 
                                on_release: print("Button 1 pressed!")  # Add your button action here
                                MDBoxLayout:  # Horizontal layout for image and label
                                    orientation: "horizontal"
                                    spacing: "4dp"  # Adjust spacing as needed
                                    Image:
                                        source: "/storage/emulated/0/python_app/rating (1).png"
                                        allow_stretch: True
                                        keep_ratio: True
                                        size_hint: (None, None)
                                        size: ("60dp", "70dp")
                                    MDLabel:
                                        text: "Rate us five star"
                                        font_style: "H6"
                                        halign: "left" 
                                        valign: "center"
                                    
                            MDCard:  # Button 1
                                orientation: "vertical"
                                padding: "10dp"
                                elevation: 1
                                size_hint_y: None 
                                height: "80dp"
                                ripple_behavior: True 
                                on_release: print("Button 1 pressed!")  # Add your button action here
                                MDBoxLayout:  # Horizontal layout for image and label
                                    orientation: "horizontal"
                                    spacing: "4dp"  # Adjust spacing as needed
                                    Image:
                                        source: "/storage/emulated/0/python_app/add-friend.png"
                                        allow_stretch: True
                                        keep_ratio: True
                                        size_hint: (None, None)
                                        size: ("60dp", "70dp")
                                    MDLabel:
                                        text: "Invite friend."
                                        font_style: "H6"
                                        halign: "left" 
                                        valign: "center"
                                        
                            MDCard:  # Button 1
                                orientation: "vertical"
                                padding: "10dp"
                                elevation: 1
                                size_hint_y: None 
                                height: "80dp"
                                ripple_behavior: True 
                                on_release: print("Button 1 pressed!")  # Add your button action here
                                MDBoxLayout:  # Horizontal layout for image and label
                                    orientation: "horizontal"
                                    spacing: "4dp"  # Adjust spacing as needed
                                    Image:
                                        source: "/storage/emulated/0/python_app/premium.png"
                                        allow_stretch: True
                                        keep_ratio: True
                                        size_hint: (None, None)
                                        size: ("60dp", "70dp")
                                    MDLabel:
                                        text: "Premium."
                                        font_style: "H6"
                                        halign: "left" 
                                        valign: "center"
                                    
                            MDBoxLayout:
                                spacing: "4dp"
                                padding: "12dp"
                                    
                            MDLabel:
                                text:"      Our Community."
                                bold: True
                                pos_hint: {'center_x':  .5}
                                
                            MDSeparator:
                                height: "1dp"
                             
                            MDCard:  # Button 1
                                orientation: "vertical"
                                padding: "10dp"
                                elevation: 1
                                size_hint_y: None 
                                height: "80dp"
                                ripple_behavior: True 
                                on_release: print("Button 1 pressed!")  # Add your button action here
                                MDBoxLayout:  # Horizontal layout for image and label
                                    orientation: "horizontal"
                                    spacing: "4dp"  # Adjust spacing as needed
                                    Image:
                                        source: "/storage/emulated/0/python_app/communicate (1).png"
                                        allow_stretch: True
                                        keep_ratio: True
                                        size_hint: (None, None)
                                        size: ("60dp", "70dp")
                                    MDLabel:
                                        text: "Contact us."
                                        font_style: "H6"
                                        halign: "left" 
                                        valign: "center"
                                    
                            MDCard:  # Button 1
                                orientation: "vertical"
                                padding: "10dp"
                                elevation: 1
                                size_hint_y: None 
                                height: "80dp"
                                ripple_behavior: True 
                                on_release: print("Button 1 pressed!")  # Add your button action here
                                MDBoxLayout:  # Horizontal layout for image and label
                                    orientation: "horizontal"
                                    spacing: "4dp"  # Adjust spacing as needed
                                    Image:
                                        source: "/storage/emulated/0/python_app/united.png"
                                        allow_stretch: True
                                        keep_ratio: True
                                        size_hint: (None, None)
                                        size: ("60dp", "70dp")
                                    MDLabel:
                                        text: "Contact us."
                                        font_style: "H6"
                                        halign: "left" 
                                        valign: "center"
                                    
                            MDBoxLayout:
                                spacing: "4dp"
                                padding: "12dp"
                                    
                            MDLabel:
                                text:"      Our Guidelines."
                                bold: True
                                pos_hint: {'center_x':  .5}
                                
                            MDSeparator:
                                height: "1dp"
                             
                            MDCard:  # Button 1
                                orientation: "vertical"
                                padding: "10dp"
                                elevation: 1
                                size_hint_y: None 
                                height: "80dp"
                                ripple_behavior: True 
                                on_release: print("Button 1 pressed!")  # Add your button action here
                                MDBoxLayout:  # Horizontal layout for image and label
                                    orientation: "horizontal"
                                    spacing: "10dp"  # Adjust spacing as needed
                                    Image:
                                        source: "/storage/emulated/0/python_app/privacy-policy.png"
                                        allow_stretch: True
                                        keep_ratio: True
                                        size_hint: (None, None)
                                        size: ("60dp", "70dp")
                                    MDLabel:
                                        text: "Privacy Policy"
                                        font_style: "H6"
                                        halign: "left" 
                                        valign: "center"
                                    
                            MDCard:  # Button 1
                                orientation: "vertical"
                                padding: "10dp"
                                elevation: 1
                                size_hint_y: None 
                                height: "80dp"
                                ripple_behavior: True 
                                on_release: print("Button 1 pressed!")  # Add your button action here
                                MDBoxLayout:  # Horizontal layout for image and label
                                    orientation: "horizontal"
                                    spacing: "4dp"  # Adjust spacing as needed
                                    Image:
                                        source: "/storage/emulated/0/python_app/insurance-policy.png"
                                        allow_stretch: True
                                        keep_ratio: True
                                        size_hint: (None, None)
                                        size: ("60dp", "70dp")
                                    MDLabel:
                                        text: "Community Guidelines"
                                        font_style: "H6"
                                        halign: "left" 
                                        valign: "center"
#Profile screen                                        
    MDScreen:
        name: "profile"
        MDBoxLayout:
            orientation: "vertical"
            spacing: "4dp"
            MDTopAppBar:
                id: "heading"
                md_bg_color: "black"
                title: "Welcome"
            ScrollView:
                orientation:"vertical"
                bar_width: 4
                MDList:
                    id: scroll_list
                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: "30dp"
                        padding: "12dp"
                        size_hint_y: None
                        height: self.minimum_height #force height calculation 
                        TwoLineIconListItem:
                            text: "Account information"  
                            #_no_ripple_effect: True
                            padding: "16dp", "16dp", "16dp", "96dp" 
                            height: "90dp"
                            secondary_text: "Now, you can edit your account basic information in including username,email and phone number"
                            IconLeftWidget:
                                icon: "account"
                                _no_ripple_effect: True
                                
                        TwoLineIconListItem:
                            text: "Password"  
                            #_no_ripple_effect: True
                            padding: "16dp", "16dp", "16dp", "96dp"  
                            secondary_text: "Change your password frequently to increase security"
                            IconLeftWidget:
                                icon: "key"
                                _no_ripple_effect: True
                        
                        TwoLineIconListItem:
                            text: "Notifications"  
                            #_no_ripple_effect: True
                            padding: "16dp", "16dp", "16dp", "96dp"  
                            secondary_text: "Turn on notifications to get information of earning"
                            IconLeftWidget:
                                icon: "bell"
                                _no_ripple_effect: True
                                
                        TwoLineIconListItem:
                            text: "Privacy policy"  
                            #_no_ripple_effect: True
                            padding: "16dp", "16dp", "16dp", "96dp"  
                            secondary_text: "Now, you can edit your account basic information in including username,email and phone number"
                            IconLeftWidget:
                                icon: "lock"
                                _no_ripple_effect: True
                                
                        
                             


#earning screen                                
    MDScreen:
        name: "earning"
    
        MDBoxLayout:
            orientation: "vertical"
            spacing: "4dp"
            MDTopAppBar:
                id: "heading"
                md_bg_color: "black"
                title: "Welcome"
                MDBoxLayout:
                    orientation: "horizontal"
                    size_hint_x: 1
                    spacing: "1dp"
                    MDLabel:
                        text: "Login Page"
                        halign: "center"
                        bold: True
                        size_hint_y: None
                        height: "40dp"
                
                    MDCard:
                        id: coin_card2
                        size: "60dp", "60dp"
                        size_hint: None, None
                        pos_hint: {"center_x": 1, "center_y": 1}  # Position the card to the top right
                    
                
                        
            MDBoxLayout:
                orientation:"vertical"
                spacing: "12dp"
                MDLabel:
                    text: "ig"
                    halign: "center"
                
                MDCard:
                    #orientation: "vertical"
                    padding: "10dp"
                    #elevation: 1
                    height: "250dp"
                    pos_hint: {'center_y': 0.9}
                    size_hint_y: None
                    #ripple_behavior: True
                    
                    MDGridLayout:
                        cols: 2
                        row: 2
                        padding: "10dp"
                        spacing: "10dp"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        MDCard:
                            id: coin_card1
                            elevation: 1
                            padding: "10dp"
                            height: "100dp"
                            on_press: app.disable1(self)
                            #pos_hint: {'center_y': 0.5}
                            size_hint_y: None
                            ripple_behavior: True
                            Image:
                                source: "/storage/emulated/0/python_app/coin.png"
                                allow_stretch: True
                                keep_ratio: True
                                size_hint: (None, None)
                                size: ("60dp", "70dp")
                                      
                        MDCard:
                            id: coin_card2
                            elevation: 1
                            padding: "10dp"
                            height: "100dp"
                            on_press:app.disable2(self)
                            #pos_hint: {'center_y': 0.5}
                            size_hint_y: None
                            ripple_behavior: True
                            Image:
                                source: "/storage/emulated/0/python_app/coin.png"
                                allow_stretch: True
                                keep_ratio: True
                                size_hint: (None, None)
                                size: ("60dp", "70dp")
                              
                                  
                        MDCard:
                            id: coin_card3
                            elevation: 1
                            padding: "10dp"
                            height: "100dp"
                            on_press:app.disable3(self)
                            #pos_hint: {'center_y': 0.5}
                            size_hint_y: None
                            ripple_behavior: True
                            Image:
                                source: "/storage/emulated/0/python_app/coin.png"
                                allow_stretch: True
                                keep_ratio: True
                                size_hint: (None, None)
                                size: ("60dp", "70dp")
                                
                            
                        MDCard:
                            id: coin_card
                            click_count: 0
                            elevation: 1
                            padding: "10dp"
                            height: "100dp"
                            on_press:app.disable(self)
                            #pos_hint: {'center_y': 0.5}
                            size_hint_y: None
                            ripple_behavior: True
                            Image:
                                source: "/storage/emulated/0/python_app/coin.png"
                                allow_stretch: True
                                keep_ratio: True
                                size_hint: (None, None)
                                size: ("60dp", "70dp")
                            
                            
             
                MDRaisedButton:
                    id: show_ad_button
                    text: "earn"
                    size_hint: (0.9, 0.13)
                    halign: "center"
                    pos_hint: {'center_x': .5}
                    on_release: app.show_rewarded_ad()

                
                
                MDBoxLayout:
                    orientation:"vertical"
                    MDTextButton:
                        id:alert_button
                        text:" "
                        pos_hint: {'center_x': .5, 'center_y': .5}
                        size_hint: (0.5, 0.13)
                        color:"red"

                            
                                       
 
'''

class Master(MDApp):
    dialog = None
    
    def home(self):
        if self.root.ids.name.text == "elly" and self.root.ids.password.text == "0000":
            self.root.current = "home"
        else:
            self.root.ids.button.text = "Wrong password or name"	
            
    def profile(self):
        self.root.current = "profile"
        
    def earning(self):
        self.root.current = "earning"
        
    def disable1(self, *args):
        self.root.ids.coin_card1.disabled = True

    def disable2(self, *args):
        self.root.ids.coin_card2.disabled = True

    def disable3(self, *args):
        self.root.ids.coin_card3.disabled = True

    def disable(self, *args):
        self.root.ids.coin_card.disabled = True

    def coins(self):
        sound = SoundLoader.load('coins.wav')
        if sound:
            sound.play()

    @mainthread 
    def show_rewarded_ad(self):
        if platform == 'android':
            from android.runnable import run_on_ui_thread
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            RewardedAd = autoclass('com.google.android.gms.ads.rewarded.RewardedAd')
            AdRequest = autoclass('com.google.android.gms.ads.AdRequest')
            FullScreenContentCallback = autoclass("com.google.android.gms.ads.FullScreenContentCallback")
            OnUserEarnedRewardListener = autoclass('com.google.android.gms.ads.rewarded.OnUserEarnedRewardListener')

            ad_unit_id = "ca-app-pub-5217449458643663/6380280632"  # Replace with your Ad Unit ID

            rewarded_ad = RewardedAd(PythonActivity.mActivity, ad_unit_id)

            @run_on_ui_thread
            def on_loaded(ad):
                print("Rewarded ad loaded.")
                rewarded_ad.setFullScreenContentCallback(FullScreenContentCallback(
                    onAdDismissedFullScreenContent=lambda *args: self.show_rewarded_ad()  
                ))
                rewarded_ad.show() 

            @run_on_ui_thread
            def on_failed_to_load(error_code):
                print(f"Rewarded ad failed to load with error code: {error_code}")
                # Retry loading with exponential backoff 
                self.retry_ad_load(rewarded_ad, on_loaded, on_failed_to_load, retry_count=1) 

            @run_on_ui_thread
            def on_reward_earned(reward_item): 
                print("User earned reward!")
                if not self.dialog: 
                    self.dialog = MDDialog(
                        title="Congratulations!",
                        text="You earned a reward!",
                        size_hint=(.8, .3)
                    )
                self.dialog.open()
                vibrator.vibrate(0.5)

            rewarded_ad.loadAd(AdRequest.Builder().build(), on_loaded, on_failed_to_load)

            # Set the reward listener *after* the ad is loaded
            rewarded_ad.setOnUserEarnedRewardListener(on_reward_earned) 

        else:
            print("Rewarded ads are only supported on Android.")

    def retry_ad_load(self, rewarded_ad, on_loaded, on_failed_to_load, retry_count=1, max_retries=3):
        if retry_count > max_retries:
            print("Max ad load retries reached. Giving up.")
            return

        delay = 2 ** retry_count  # Exponential backoff (2, 4, 8... seconds)
        print(f"Retrying ad load in {delay} seconds...")
        Clock.schedule_once(lambda dt: rewarded_ad.loadAd(
            AdRequest.Builder().build(), on_loaded, on_failed_to_load
        ), delay)
        
    def build(self):        
        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        #self.show_ad_button = self.root.ids.show_ad_button
        #self.show_rewarded_ad()
        
        return Builder.load_string(kv)
	       

Master().run()
