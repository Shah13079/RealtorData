import subprocess

# Define the list of states with their corresponding state codes
states = [
    # {'name': 'Florida', 'code': 'FL'},
    # {'name': 'Arizona', 'code': 'AZ'}, 
    # {'name': 'California', 'code': 'CA'},
    # {'name': 'Colorado', 'code': 'CO'},
    # {'name': 'Connecticut', 'code': 'CT'},         
    
    # {'name': 'Georgia', 'code': 'GA'},
    # {'name': 'Hawaii', 'code': 'HI'},             
    # {'name': 'Illinois', 'code': 'IL'},
    
    # # =============================================


    # {'name': 'Alabama', 'code': 'AL'},
    # {'name': 'Alaska', 'code': 'AK'},          
    # {'name': 'Arkansas', 'code': 'AR'},  
    # {'name': 'Iowa', 'code': 'IA'},    
    ##==================================================== ye sab window main load hai
    {'name': 'Texas', 'code': 'TX'},
    {'name': 'Kentucky', 'code': 'KY'},
    {'name': 'Indiana', 'code': 'IN'},
    {'name': 'Louisiana', 'code': 'LA'},
    {'name': 'Maryland', 'code': 'MD'},
    
    # # ================================================

    # {'name': 'Michigan', 'code': 'MI'},
    # {'name': 'Minnesota', 'code': 'MN'},
    # {'name': 'Missouri', 'code': 'MO'},
    # {'name': 'Nevada', 'code': 'NV'},
    # {'name': 'New Jersey', 'code': 'NJ'},

    # # =====================================================

    # {'name': 'New York', 'code': 'NY'},
    # {'name': 'North Carolina', 'code': 'NC'},
    # {'name': 'North Dakota', 'code': 'ND'},
    # {'name': 'Ohio', 'code': 'OH'},

    # # ----------------------------------------------------

    # {'name': 'Oklahoma', 'code': 'OK'},
    # {'name': 'Oregon', 'code': 'OR'},
    # {'name': 'Pennsylvania', 'code': 'PA'},
    # {'name': 'South Carolina', 'code': 'SC'},

    #=======================================================

    # {'name': 'Tennessee', 'code': 'TN'},
    # {'name': 'Utah', 'code': 'UT'},
    # {'name': 'Virginia', 'code': 'VA'},
    # {'name': 'Washington', 'code': 'WA'},
    


# ----------------In states Runner--------------------------
    # {'name': '    ', 'code': 'KS'},               #Small
    # {'name': 'Maine', 'code': 'ME'},                #small
    # {'name': 'Massachusetts', 'code': 'MA'},        #small
    # {'name': 'Delaware', 'code': 'DE'},             #small
    # {'name': 'Idaho', 'code': 'ID'},                #Small
    # {'name': 'Rhode Island', 'code': 'RI'},         #small      
    # {'name': 'Mississippi', 'code': 'MS'},          #small
    # {'name': 'Montana', 'code': 'MT'},              #small
    # {'name': 'Nebraska', 'code': 'NE'},             #small
    # {'name': 'New Mexico', 'code': 'NM'},           #small
    # {'name': 'South Dakota', 'code': 'SD'},         #Small
    # {'name': 'New Hampshire', 'code': 'NH'},        #small
    # {'name': 'West Virginia', 'code': 'WV'},        #small
    # {'name': 'Wyoming', 'code': 'WY'}               #small
    # {'name': 'Vermont', 'code': 'VT'},              #small
    # {'name': 'Wisconsin', 'code': 'WI'},            #small
]

# Iterate through each state
for state in states:
    state_name = state['name']
    state_code = state['code']

    # Define the command to execute the spider in CMD
    command = f"scrapy crawl condos -o {state_code}.csv -a state_name=\"{state_name}\" -a state_code={state_code}"

    # Execute the command in CMD
    subprocess.run(command, shell=True, check=True)

    # Print status message
    print(f"Spider for {state_name} ({state_code}) completed.\n")

print("All spiders have been executed.")


