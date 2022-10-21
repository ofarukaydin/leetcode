#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#

# @lc code=start
class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = Node(homepage)

    def visit(self, url: str) -> None:
        node = Node(url)
        node.prev = self.root
        self.root.next = node
        self.root = self.root.next

    def back(self, steps: int) -> str:
        while (steps and self.root.prev):
            self.root = self.root.prev
            steps -= 1
        return self.root.val

    def forward(self, steps: int) -> str:
        while (steps and self.root.next):
            self.root = self.root.next
            steps -= 1
        return self.root.val

browserHistory = BrowserHistory("leetcode.com");
browserHistory.visit("google.com")     #You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com")   #You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com")    #You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1)                 #You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1)                 #You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1)              #You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com")   #You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2)              #You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2)                 #You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7)                 #You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"


        # @lc code=end
