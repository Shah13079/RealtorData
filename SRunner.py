import subprocess

# Define the list of states with their corresponding state codes
states = [
    # {'name': 'Kansas', 'code': 'KS'},               
    # {'name': 'Maine', 'code': 'ME'},                
    # {'name': 'Massachusetts', 'code': 'MA'},        
    # {'name': 'Delaware', 'code': 'DE'},   
    
              
    # {'name': 'Idaho', 'code': 'ID'},                
    # {'name': 'Rhode Island', 'code': 'RI'},               
    # {'name': 'Mississippi', 'code': 'MS'},          
    # {'name': 'Montana', 'code': 'MT'},              
    # {'name': 'Nebraska', 'code': 'NE'},           


    # {'name': 'New Mexico', 'code': 'NM'},           
    # {'name': 'South Dakota', 'code': 'SD'},         
    # {'name': 'New Hampshire', 'code': 'NH'},        
    # {'name': 'West Virginia', 'code': 'WV'},  
       
    # {'name': 'Alabama', 'code': 'AL'},
    # {'name': 'Alaska', 'code': 'AK'},
    # {'name': 'Arizona', 'code': 'AZ'},

    
    # {'name': 'Arkansas', 'code': 'AR'},
    # {'name': 'California', 'code': 'CA'},
    # {'name': 'Colorado', 'code': 'CO'},

    # {'name': 'Connecticut', 'code': 'CT'},
    # {'name': 'Florida', 'code': 'FL'},
    # {'name': 'Georgia', 'code': 'GA'},
    # ------------------------------------------


    # {'name': 'Hawaii', 'code': 'HI'},
    # {'name': 'Illinois', 'code': 'IL'},

    # {'name': 'Indiana', 'code': 'IN'},
    # {'name': 'Iowa', 'code': 'IA'},
    # {'name': 'Kentucky', 'code': 'KY'},
    # {'name': 'Louisiana', 'code': 'LA'},
    # {'name': 'Maryland', 'code': 'MD'},

    # # -----------------------------------------------
    
    # >>>This is one
    # {'name': 'Michigan', 'code': 'MI'},
    # {'name': 'Minnesota', 'code': 'MN'},
    # {'name': 'Missouri', 'code': 'MO'},
    # {'name': 'Nevada', 'code': 'NV'},


    # {'name': 'New Jersey', 'code': 'NJ'},
    # {'name': 'New York', 'code': 'NY'},
    # {'name': 'North Carolina', 'code': 'NC'},
    # {'name': 'North Dakota', 'code': 'ND'},
    # {'name': 'Ohio', 'code': 'OH'},
    # {'name': 'Oklahoma', 'code': 'OK'},

    # # ---------------------------------------------------

    # {'name': 'Texas', 'code': 'TX'},
    # {'name': 'Oregon', 'code': 'OR'},
    # {'name': 'Pennsylvania', 'code': 'PA'},
    # {'name': 'South Carolina', 'code': 'SC'},
    # {'name': 'Tennessee', 'code': 'TN'},
    
    # ------------------------------------------------------
    # {'name': 'Utah', 'code': 'UT'},
    # {'name': 'Vermont', 'code': 'VT'},
    # {'name': 'Virginia', 'code': 'VA'},
    # {'name': 'Washington', 'code': 'WA'},
    # {'name': 'Wisconsin', 'code': 'WI'},
    # {'name': 'Wyoming', 'code': 'WY'}
]





# Iterate through each state
for state in states:
    state_name = state['name']
    state_code = state['code']

    # Define the command to execute the spider in CMD
    command = f"scrapy crawl states -o {state_code}.csv -a state_name=\"{state_name}\" -a state_code={state_code}"

    # Execute the command in CMD
    subprocess.run(command, shell=True, check=True)

    # Print status message
    print(f"Spider for {state_name} ({state_code}) completed.")

print("All spiders have been executed.")