# https://leetcode.com/problems/subdomain-visit-count/
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_dict = dict()
        for cpdomain in cpdomains:
            cp,domain = cpdomain.split(" ")
            cp = int(cp)
            domain = list(domain.split("."))
            while(len(domain)>0):
                if ".".join(domain) not in domain_dict:
                    domain_dict[".".join(domain)] = cp
                else:
                    domain_dict[".".join(domain)] += cp
                domain.remove(domain[0])
        l = list()
        for k in domain_dict.keys():
            l.append(str(domain_dict[k])+" "+k)
        return l

def test():
    """

    :return:
    """
    s = Solution()
    s.subdomainVisits(["9001 discuss.leetcode.com"])
    # ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
    s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])
    # ["901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org", "1 intel.mail.com", "951 com"]

if __name__ == "__main__":
    test()
    # test1()
    # test2()
    # test3()