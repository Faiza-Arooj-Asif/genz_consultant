# genz_consultant
> *Why ask ChatGPT when you can consult a script with zero patience and maximum attitude?
A dummy AI-powered decision maker that gives you unvarnished truth, big vibes, and zero fluff in y. Ask it anything when you're feeling indecisive. No cap!

What new I have learnt:
**flush=True**

print() usually writes to a buffer first.
flush=True tells Python: “send this output to the terminal immediately, don’t wait.”
This is useful for progress indicators like:
print(".", end="", flush=True)
Without flush, the dots may appear all at once after the loop, or not show in real time.
So it makes the “thinking...” animation feel smooth.
**name == "main"**

Python sets a special variable called name automatically.

When a file is run directly, name is "main"

When the file is imported from another file, name is the module’s name instead

So this line:

if name == "main":
ask_ai()