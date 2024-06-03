import pickle

def saveModelToFile(model, filename):

    try:
        with open(filename , 'w', encoding ='utf8') as f: 
            pickle.dump(model, f) 
        print ("Game saved under " + f)
    except Exception as e:
        print (e)
        print ("Not able to save model!")


def loadModelFromFile(filename):
    model = None
    try:
        with open(filename) as f:
            model = pickle.load(f)
        print ("Model loaded")
    except Exception as e:
        print (e)
        print ("Not able to load model!")
        
    return model