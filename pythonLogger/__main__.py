import os
import sys
import string
import logging
import time
from random import choices
from logging import basicConfig
from functools import partial, partialmethod



A = 0
avgFindImp = 0
average = []

#counting time
#Decorator function that measure the execution time of the provided function.
def measure_ops(func):
    def inner(*args, **kwargs):
        startTimeD = time.time()
        return_val = func(*args, **kwargs)
        endTimeD = time.time()
        
        execTime = round(endTimeD - startTimeD, 3)
        print(f"Function `{func.__name__}` executed in {execTime} seconds.")
        return return_val
    return inner


startRead = time.time()
endRead = time.time()
startWrite =time.time()
endWrite = time.time()
startFind = time.time()
endFind = time.time()
startTime = time.time()
endTime = time.time()
dif = round(endTime - startTime, 3)
dif2 = endTime - startTime

#create and configure trace
logging.TRACE = 60
logging.addLevelName(logging.TRACE, 'TRACE')
logging.Logger.trace = partialmethod(logging.Logger.log, logging.TRACE)
logging.trace = partial(logging.log, logging.TRACE)
log_level = logging.TRACE


#creating file for logging input and its format
LOG_FORMAT = "%(levelname)s %(asctime)s, in line [%(lineno)d] - %(message)s"
logging.basicConfig(filename = "consoleapp.log", level = logging.DEBUG, format = LOG_FORMAT, filemode='w')

#calling logger method to create logging object
logger = logging.getLogger()



@measure_ops
def main():   
    print("Welcome! ")
    logger.trace("Start tracing in main ")
    logger.info(" Starting application...")
    
    #assign CLI intake 
    args = sys.argv[1:]
    
    # Ask for the file directory input
    logging.debug("Prompting user for directory path")
    filePath = input("Please enter the path or file name if in the same directory: ")
    if filePath == "":
        logging.error("User did not enter the path")
        filePath = input("Please enter the path this time or file name if in the same directory: ")
    elif (os.path.isfile(filePath)) == False:
        logging.critical("User enterred wrong path")
        filePath = input("The path you entered is not correct, please enter again the path or file name if in the same directory: ")
    readOWrite = input("Please specify if you want to read  or write the file: ") 
    
    logging.debug(f"File path: {filePath}")
    logging.debug(f"File read/write: {readOWrite}")
    print(f"you entered this path: {filePath}")
    
    args[0:] = "" + readOWrite
    args[1] = "" + filePath
    
    #looping according to users input read or write
    if(args[0].lower() == "w"):
        startTime
        logger.info(f"start counting time: {startTime} " )
        writeFile(args[1])
    elif(args[0].lower() == 'r'): 
        startTime   
        logger.info(f"start counting time: {startTime} " )
        readFile(args[1])
    else:
        print("Command not Recognized: please use 'write' or 'read'")
        logging.error("User is not entering write or read")
    endTime
    logger.info(f"stops counting the time at: {endTime} ")

    #performance time - stored in array and being called
    admin = input("Do you want the report with performance time? y or n ")
    if admin.lower() == "y":
        print(f"the execution time was: {dif2}")
        if args[0].lower() == 'r':
            #Average time to read a line from the file
            print("Average time to read a line from the file is ", average[0])
            #Average time to find the word "imperdiet" in the line
            print("Average time to find the word 'imperdiet' in the line ", average[1])
        else:
            #Average time to write a line in the file
            print("Average time to write a line in the file ", average[0] )
            #Average time to find the word "imperdiet" in the line
            print("Average time to find the word 'imperdiet' in the line ", average[1] )
    logger.trace("the end of main entry block, finishing the application ")
        
@measure_ops       
def writeFile(filePath):
    logger.trace("start writeFile block ")
    startTime
    logger.info(f"start counting time: {startTime} " )
  
    counter=0
    lineCounter=0
    sum = 0
    avgFindImp=0

    var = open(filePath,"w")
    #prompting user for sentence
    logging.debug("Prompting user for directory path")
    sentence = input("Please enter a sentence and hit enter: ")    
    sentenceCounter = 1

    if sentence.count("imperdiet") > 0:
        endFind
        counter += sentence.count("imperdiet")
        lineCounter += 1
        found = endFind - startFind
        sum = sum + found
        avgFindImp = sum / counter
    startWrite
    var.write(sentence)
    endWrite
    logging.debug("Prompting user for another sentence")
    nextline = input("Would you like to enter more sentences? Yes or No?")
    if nextline.lower() == "n":
        logging.error("user entered n")
        print("next time please type both letters")
        nextline = "no"
    if nextline.lower().isnumeric():
        logging.error("user entered number!")
        print("hmmm , please no numbers unless in the sentence ")    
    while nextline.lower() != "no":
        logger.debug("in write while loop")
        sentenceCounter += 1
        logging.debug("Prompting user for another sentence")
        sentence = input("Please enter a sentence and hit enter ")
        if sentence.count("imperdiet") > 0:
            counter += sentence.count("imperdiet")
            lineCounter +=1
        var.write(sentence)
        logging.debug("Prompting user for another sentence")
        nextline = input("Would you like to enter more sentences? Yes or No ")
        if nextline.lower() == "n":
            logging.warning("user entered n")
            print("next time please type both letters")
            nextline = "no"
        elif nextline.lower().isnumeric():
            logging.error("user entered number!")
            print("hmmm , we need yes or no ")   
    found = endWrite - startWrite
    sum = sum + found
    avgWriteLine = sum / sentenceCounter

      
    print("You have enter this amount of sentences: ", sentenceCounter)
    print("The number of times the word imperdient appears in the user input: ", counter ) 
    print("The number of sentences with the word imperdient: ", lineCounter )

    C = format(avgWriteLine, '.6e')
    average.append(C)
    
    D = format(avgFindImp, '.6e')
    average.append(D)
    
    var.close()   
    logger.trace("end of writeFile block ")

@measure_ops
def readFile(filePath):
    logger.trace("in readFile block ")
    

    counter = 0
    linecounter = 0
    countLines = 0
    readLine = 0
    avgFindCounter = 0
    sum = 0
    suma = 0
    var = open(filePath,"r")
    file = var.readline()
    
    
    while file != "":
        startFind
        wordcount = file.count("imperdiet")
        counter += wordcount
        if wordcount > 0:
            linecounter += 1
            endFind
            found = endFind - startFind
            sum = sum + found
            avgFindImp = sum / linecounter
        startRead    
        file = var.readline()
        endRead
        countLines += 1
        readLine = endRead - startRead
        sum = sum + readLine
        
        avgReadLine = sum / countLines
    #A = '{:f}'.format(avgReadLine)
    A = format(avgReadLine, '.6e')
    average.append(A)
        
        
    B = format(avgFindImp, '.6e')
    average.append(B)
     
    print("The number of times the word imperdient exist in file is: ", counter ) 
    print("The number of lines with the word imperdient: ", linecounter )
    print("Amount of lines ", countLines )
    
    var.close()   
    logger.trace("end of readFile block")


if __name__ == "__main__":
    
    # The main program starts here
    main()