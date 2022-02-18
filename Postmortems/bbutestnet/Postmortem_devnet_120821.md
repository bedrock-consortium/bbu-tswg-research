## Postmortem DevNet 12/08/21

### Attendance

Nat Halloway (USAA)
Praneel Pallegar (CVS)
Aaron Reed (IBM)

### Activity

This was an attempt to add the CVS nodes to the developer network.

### Environment

At the the moment of onboarding, we had 4 reachable nodes (USAA, Daon, Lumedic, IBM).

### What Happened

CVS is trying to bring up a node using the Blockchain Automation Framework (BAF).  This is in an effort to try to find an easier path toward provisioning a node for the network.

This was our first attempt ever to add a node to the network.  Praneel went through the BAF process to provision a node and we all performed connectivitity tests with his node and all of the nodes on the network.

Nat tried to write the information to the ledger but was unable to, receiving an error about the number of signatures necessary for the transaction.  Aaron investigated the auth rules on the network and Indy documentation and determined that for our developer network a single Trustee can add a steward to the network.  Aaron was able to write the steward DID and verkey to the ledger for CVS.

After adding the DID and verkey to the ledger, we left Praneel to start up his node and finish testing, etc.  By 9:45am the next day, we were getting notified that writes to the ledger were failing.

### Lessons Learned

Lynn helped us get back into consensus and he mentioned these weaknesses in our approach:

* we should have all visually verified that the network was in consensus after the node was added to the network, actively watching consensus and our node logs for at least 15 minutes after the node was added and occassionally for the next hour afterwards, looking for problems.
* we should have done screen sharing and run through the checklist with Praneel instead of trusting that he had configured everything the same way that we did.  Especially since this was a BAF environment.  It turns out that he was not using the Sovrin packages (which is fine, just inconsistent with the rest of us).  But the version of Indy node was 1.12.1 while the rest of us were running 1.12.4.  Which isn't necessarily a problem.  But as Lynn said, it is much easier to get consistent results with consistent environments. 

