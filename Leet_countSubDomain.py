
import collections
def subdomainVisits(cpdomains):
    out = collections.Counter()
    for sub in cpdomains:
        count, domains = sub.split()
        count = int(count)
        frags = domains.split('.')
        for i in range(len(frags)):
            out['.'.join(frags[i:])] += count
    return ['{} {}'.format(ct, dm) for dm, ct in out.items()]


a = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
subdomainVisits(a)
