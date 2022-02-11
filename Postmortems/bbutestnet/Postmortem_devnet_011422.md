## Postmortem DevNet 01/14/22

### Attendance

Lynn Bendixsen (Indicio)
Nat Halloway (USAA)
Moises Jaramillo (Lumedic)
Nick McGough (Daon)
Praneel Pallegar (CVS)
Aaron Reed (IBM)

### Activity

This was our second attempt to add the CVS nodes to the developer network.  Praneel had worked with people from Accenture to get Indy node code to version 1.12.4.

### Environment

At the the moment of onboarding, we had 4 reachable nodes (USAA, Daon, Lumedic, IBM).

### What Happened

CVS is trying to bring up a node using the Blockchain Automation Framework (BAF).  This is in an effort to try to find an easier path toward provisioning a node for the network.

Praneel went through the BAF process to provision a node and performed connectivitity tests with all of the nodes on the network.

Due to the nature of the BAF environment, Praneel had issues directly accessing the machine and discovering information about it in order to sanity check the environment that the node will be running in.  Much of the configuration is done using scripts or config files that BAF processes.  Because of this, very little could be verified using screen sharing.  We had to trust that BAF would process the values correctly and in a way that is consistent with the other deployed machines on the network.  Lynn and Praneel had, to the best of their ability, tried to determine that the sanity checks of the environment passed.

Aaron (IBM) wrote the steward DID and verkey to the ledger for CVS.

Immediately after Praneel started the node, Moises noticed that the network was out of consensus.

### Lessons Learned

Lynn mentioned this weakness in our approach:

* we should have all visually verified that the network was in consensus prior to starting the node.  We had assumed it was since the write of the Steward node succeeded.
* the Lumedic node had been having some connectivity issues earlier, but seemed find after it was restarted.  We probably should have been more patient in determining whether the network was stable.

In addition, this would also probably be wise:

* Lynn mentioned that we should really have a monitor on the network to alert us when nodes go down, when consensus has been lost or nodes become unreachable.  That would give us much more insight to the health and stability of our network.
* our inexperience with the technology makes it harder for us to recognize an error when it happens and take the appropriate actions.  Once the network has lost consensus, it is too late.
* Praneel noted that using BAF in this way is new, usually when BAF is used in a network, BAF is used to provision every node in the network.
* Lynn suggested that if we want to continue with BAF, that we build a test network and then let the CVS BAF node join that.  It is a safer approach to working out the kinks.