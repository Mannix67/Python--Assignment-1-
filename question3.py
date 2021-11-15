def  play_tennis(
        outlook, humidity, windy):
    
    """This function decide if members should play tennis or not.
    It returns yes , no or unknown as output.
    
    Keyword arguments:
        outlook -- tooks sunny, overcast or rainy as input
        humidity -- tooks high or normal as input
        windy -- tooks true or false as input
        
        """
    
    
    # checking if inputs are correct or not. if none of the conditions are met for outlook , humidity or wind, then the value is going to be unknown.
    if(outlook != "overcast" and  outlook != "sunny" and  outlook != "rainy"):
        return "Unknown outlook value"
    elif(humidity != "high" and humidity != "normal"):
        return "Unknown humidity value"
    elif(windy != "true" and  windy != "false"):
        return "Unknown windy value"
    
    
    
    #taking decission and returning the output.  using == as we are comparing rather than assigning.
    elif outlook == "overcast":
        return "yes"
    
    elif outlook == "sunny" :
        if humidity == "high":
            return "no"
        else:
            return "yes"

    elif outlook == "rainy":
        if windy == "false":
            return "yes"
        else :
            return "no"



print("outlook=sunny, humidity=high, windy=true play tennis?",play_tennis(outlook="sunny",humidity="high",windy="true"))
print("outlook=overcast, humidity=high, windy=false play tennis?",play_tennis(outlook="overcast",humidity="high",windy="false"))
print("outlook=rainy, humidity=high, windy=false play tennis?",play_tennis(outlook="rainy",humidity="high",windy="false"))
print("outlook=xyz, humidity=high, windy=false play tennis?",play_tennis(outlook="xyz",humidity="high",windy="false"))
print("outlook=sunny, humidity=xyz, windy=false play tennis?",play_tennis(outlook="sunny",humidity="xyz",windy="false"))
print("outlook=sunny, humidity=high, windy=xyz play tennis?",play_tennis(outlook="sunny",humidity="high",windy="xyz"))