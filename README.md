# D2L Quiz Converter
This tiny python script can be used to convert the html randomly generated questions created by [CheckIt](https://github.com/stevenclontz/checkit) 

## Usage
To use this script first create a file with the html coded questions (following the format from [CheckIt](https://github.com/stevenclontz/checkit)) in the same folder/file location as this script. Then in your terminal (or how else you use python files)

```>python quiz_converter_d2l.py```

Then the program will prompt you as follows:

```what bank file to convert: ```
Here you will type the name of the file you saved the html code from [CheckIt](https://github.com/stevenclontz/checkit)

Next you will be prompted with:

```what name for the file of the quiz:```
Here you will type the name you want to name the output file which will be automatically created in the same folder as the program and the bank questions. You should NOT add an extension to this name as D2L will only accept files with the .csv extension so the program will already format your file in this way.

Next you will be prompted with:

```what do you want ot title these type of questions:```
here you will type a title for these type of questions. The program will automatically give each question from the bank file this title appended with the number in which appears in the bank file.

Once you have filled out all of these prompts and hit return your file is ready for upload. 

## Uploading in D2L

In D2L you will need to navigate to your course shell, then go to Assessments > Quizzes > Question Library > Import > Upload a File

Then you can either drag and drop your file into the pop-up loader or click Browse Files and navigate to your file.
