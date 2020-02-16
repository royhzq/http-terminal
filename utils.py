import subprocess
        
def exec(cmd):
    """Given terminal command in string, execute bash command.

    Args
        cmd (str): Command line string
    Returns
        output (tuple): tuple containing str for stdout and stdin
    """

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
    )

    # while True:
    #     output = process.stdout.readline()
    #     print(output)   
    #     # Do something else
    #     return_code = process.poll()
    #     if return_code is not None:
    #         # Process has finished, read rest of the output 
    #         for output in process.stdout.readlines():
    #             print(output)
    #         break
                
    stdout, stderr = process.communicate()
    if stdout:
        stdout = stdout.decode('utf-8').split('\r\n')
        for line in stdout: print(line)
    else:
    	stdout = []

    if stderr:
        stderr = stderr.decode('utf-8').split('\r\n')
        for line in stderr: print(line)
    else:
    	stderr = []

    return stdout, stderr


