## Postmortem DevNet 01/25/22

### Activity

We were trying to add two USAA nodes to the developer network.

### Attendance

Nat Halloway (USAA)
Nick McGough (Daon)
Aaron Reed (IBM)

### Environment

At the the moment of onboarding, we had 3 reachable nodes (USAA, Daon, IBM), all in consensus.  Lumedic was having issues connecting to IBM so was offline trying to resolve networking problems.

### What Happened

USAA had two new virtual machines that were to be added as nodes on the ledger, all running the correct levels of Indy Node and Sovrin packages and brought up using successful instructions from previous USAA onboarding.  VMs running in the USAA cloud.  Nat (USAA) unable to share screen on the Zoom call so typical onboarding where multiple eyes can verify setup not possible.

Nat had already setup DID and verkey for both nodes.  We decided to add only one node at a time.  DID and verkey pair for server02 was written to the ledger with steward role by Aaron (IBM).  Nat started the node.  The existing nodes started getting errors.  Per Nat, "I ended up trying to start the 03 server instead of the 02 server. The IPs and keys mismatched. I had too many terms open on a little screen".

We believe that when Nat ran `ledger node target=<node_identifier> node_ip=<validator_node_ip_address> node_port=<node_port> client_ip=<validator_client_ip_address> client_port=<client_port> alias=<validator_alias> services=VALIDATOR blskey=<validator_bls_key> blskey_pop=<validator_bls_key_pop>` using server02 values but then went to the terminal for server03 and ran `sudo systemctl start indy-node`, then a node not registered to the ledger was making requests of the other nodes on the network causing issues.  Because we only had 3 nodes in consensus, when one of them started suffering errors, the network got out of consensus.

As a side note, the two USAA VMs, due to excentricity of the USAA cloud, unable to respond to each other.

### Lessons Learned

After discussing what went wrong with Lynn Bendisxson (Indicio), he mentioned these weaknesses in our approach:

* we should not have attempted this without all 4 genesis nodes healthy and connected to the network and all of them being in consensus.  Without that, the network is too brittle.

In addition, this would also probably be wise:

* the node joining the network should have been screen sharing when going through the checklist, perhaps then we would have noticed the IP address issue earlier.
* our inexperience with the technology makes it harder for us to recognize an error when it happens and take the appropriate actions.  Once the network has lost consensus, it is too late.
* Nick was taking some time off the 3 days after this attempt to add a node.  When we had the failure and lost consensus, we all stopped our nodes, cleared the network information from our nodes, and restarted our nodes.  We ended up not reaching consensus and then Nick was unreachable for most of the next two days before being able to get back online and help us get consensus back with Lynn's help.  In the future we need to schdule node additions with an eye on everyone's availability.  We should probably broadcast when we schedule it so anyone with demos, etc. can take appropriate actions.