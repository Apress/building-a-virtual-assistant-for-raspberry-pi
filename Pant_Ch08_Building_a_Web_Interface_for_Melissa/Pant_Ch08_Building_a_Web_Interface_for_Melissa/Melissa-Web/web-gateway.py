import os
import yaml
import web

from GreyMatter.SenseCells.tts import tts

render = web.template.render('templates/')

urls = (
    '/', 'index',
)

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# Functioning Variables
name = profile_data['name']

tts('Welcome ' + name + ', systems are now ready to run. How can I help you?')

class index:
    def GET(self):
        return render.index()
        
    def POST(self):
        x = web.input(myfile={})
        filedir = os.getcwd() + '/uploads' # change this to the directory you want to store the file in.
        if 'myfile' in x: # to check if the file-object is created
            filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            fout = open(filedir +'/'+ filename,'w') # creates the file where the uploaded file should be stored
            fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
            fout.close() # closes the file, upload complete.
        os.system('python main.py ' + filename)
        
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()