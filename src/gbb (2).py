import subprocess

def gobust(url, wrdlist):

        cmd = ['gobuster', 'dir', '-u', url, '-w', wrdlist]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)


        while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                        break
                if output:
                        print (output.strip())


        if process.returncode != 0:
                error = process.stderr.read().strip()
                print (f'Error: {error}')


n = input(f'Enter IP:')
target_url = 'http://' + n
wordlist_file = '/usr/share/wordlists/dirb/common.txt'
gobust(target_url, wordlist_file)

