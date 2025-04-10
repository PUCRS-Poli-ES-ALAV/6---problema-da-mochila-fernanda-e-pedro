iters = 0

def ED(S: str, T: str, i: int, j: int) -> int:
    global iters
    iters += 1
    s = S[:i]
    t = T[:j]
    
    if not s and not t:
        return 0
    if s and not t:
        return len(s)
    if t and not s:
        return len(t)

    if s[i-1] == t[j-1]:
        return ED(s, t, i-1, j-1)

    sub = ED(s, t, i-1, j-1) + 1
    insert = ED(s, t, i, j-1) + 1
    remove = ED(s, t, i-1, j) + 1

    return min(sub, insert, remove)

# s1 = "Casablanca"
# s2 = "Portentoso"

s1 = "".join(["Maven, a Yiddish word meaning accumulator of knowledge, began as an attempt to " ,
   			"simplify the build processes in the Jakarta Turbine project. There were several" , 
   			" projects, each with their own Ant build files, that were all slightly different." ,
   			"JARs were checked into CVS. We wanted a standard way to build the projects, a clear ", 
   			"definition of what the project consisted of, an easy way to publish project information" ,
   			"and a way to share JARs across several projects. The result is a tool that can now be" ,
   			"used for building and managing any Java-based project. We hope that we have created " ,
   			"something that will make the day-to-day work of Java developers easier and generally help " ,
   			"with the comprehension of any Java-based project."])
s2 = "".join(["This post is not about deep learning. But it could be might as well. This is the power of " ,
   			"kernels. They are universally applicable in any machine learning algorithm. Why you might" ,
   			"ask? I am going to try to answer this question in this article." , 
   		        "Go to the profile of Marin Vlastelica Pogančić" , 
   		        "Marin Vlastelica Pogančić Jun"])

res = ED(s1, s2, len(s1), len(s2)) 
print(res)
    
print(iters)
