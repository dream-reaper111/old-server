

https://github.com/user-attachments/assets/bf652f4e-4eb0-4b55-b422-e37e79d47347

# old-server
old server from my teenage years 2015-2017 only god knows what I was up too 



The NULLSEC Archives · 2015–2017
</div>

This repository preserves early programming experiments from 2015–2017: TCP sockets, a desktop chat interface, threaded connections, custom message encryption, and a collection of Windows API functions.
It captures the learning process as it happened—rough drafts, ambitious ideas, unfinished functions, colorful comments, and plenty of things a future version would do differently.
Treat this as a historical source archive. The files are not a tested application release, and several contain syntax errors, missing dependencies, or security-sensitive behavior.
Inside the archive
File	What it contains	Current caveats
[`nullserv.py`](nullserv.py)	Threaded TCP chat server with message broadcasting, a shared initialization check, AES-CBC routines, and NULLSEC terminal branding.	Legacy Python 2; custom cryptography and concurrency issues.
[`nullF.py`](nullF.py)	PyQt4 desktop chat client with a message list, text input, send button, and disconnect control.	Legacy Python 2/PyQt4; GUI updates occur from a background thread.
[`server.py`](server.py)	A collection of early TCP server/client and echo experiments.	Contains substantial syntax, indentation, and API errors; not executable as committed.
[`nullframework.cpp`](nullframework.cpp)	Windows API experiments for keyboard/mouse input, display control, process commands, and system-level behavior.	Incomplete source collection; references a missing stdafx.h and has no main() entry point.


NULLSEC chat experiments
The Python chat pair uses a central server to relay messages between connected clients. Both files point to the loopback address 127.0.0.1 on port 4445 in the committed source.
The implementation explores:
- TCP connections and timeout-based receive loops.
- A thread-based model for connected users and message handling.
- A PyQt4 interface generated from an earlier nullchat.ui file.
- AES-CBC encryption with random initialization vectors and Base64 encoding.
- SHA-512-based key derivation and a deterministic key-update sequence.
- An initialization exchange and client display name.
- Terminal banners through pyfiglet and terminal handling through colorama.
These are implementation details, not guarantees of secure messaging. The server decrypts messages before relaying them, so the design does not provide end-to-end encryption.
What time taught this code
Encryption needs a complete security design
The chat source embeds shared key material and a static initialization check. Its AES-CBC messages have no accompanying MAC or authenticated-encryption tag. Repeatedly hashing a shared key does not establish forward secrecy or authenticated identities.
TCP needs explicit message boundaries
The receive routines use timeouts to collect bytes rather than a defined message frame. TCP can split or combine application messages, and calls to send() do not guarantee that the entire supplied buffer was sent.
Threads need ownership and coordination
The server starts two receive handlers for the same connection, shares mutable user and key state, and creates additional threads during message processing. The GUI client also updates Qt widgets from its listener thread. These patterns make ordering, shutdown, and synchronization fragile.
An archive is allowed to show unfinished work
server.py preserves overlapping socket exercises rather than a coherent runnable program. The C++ source collects functions rather than a complete buildable project. Keeping those distinctions visible makes the repository a more honest record of learning.
Windows source notes
nullframework.cpp is separate from the chat application; the inspected files do not establish an integration between them.
It includes input simulation, cursor positioning, monitor control, shell-command execution, an input-blocking wrapper, a system-crash routine, and an account-management sequence. Those functions can affect system stability or configuration if incorporated into an executable and invoked.
Some names and comments overstate the implementation. For example, MBRDie() opens and closes a physical-drive handle but contains no disk-write call. Likewise, simulated elevation keystrokes do not establish an automatic UAC bypass.
Review this file as source in an isolated environment. This archive does not provide a deployment guide for its disruptive functions.
Historical dependencies
Component	Dependencies referenced in source
Chat server	Python 2, Crypto AES/Random APIs, colorama, pyfiglet, standard-library sockets and threading.
Desktop client	Python 2, PyQt4, Crypto AES/Random APIs, pyfiglet, standard-library sockets and threading.
Windows experiments	Windows SDK APIs, ntdll.lib, and a referenced stdafx.h that is absent from this repository.


The repository does not supply pinned dependency versions, a requirements file, the original Qt Designer file, a complete C++ project, automated tests, or a reproducible build. Python 3 compatibility would require code changes.
A possible next chapter
If the chat project is revisited, a clean successor could preserve the NULLSEC identity while using a modern foundation:
1. Preserve the archive: retain the original files and document their history.
2. Rebuild the chat core: use Python 3, explicit message framing, bounded messages, and predictable connection cleanup.
3. Use established transport security: replace the custom cryptographic protocol with TLS and a documented authentication design.
4. Refresh the desktop interface: use a maintained Qt binding and signals for updates on the GUI thread.
5. Add useful validation: test fragmented messages, simultaneous clients, malformed input, and disconnect handling.
6. Package the successor: document dependencies, configuration, local development, and a clear supported scope.
These are future ideas, not features implemented in the archived code.
Credits and provenance
The existing repository description identifies this as work from the owner's teenage years, 2015–2017. The nullserv.py header credits Taipan.py(me) and NullByte.py(miss you buddy), with a project start date of April 11, 2017. The generated client header is dated April 24, 2017 and identifies the PyQt4 UI code generator.
Preserve those credits when documenting or adapting the source.
License
No license file was present in the repository root at the time of review. This README does not assign a license or establish ownership of individual contributions.
<div align="center">

A time capsule of curiosity, late-night code, Pizza, breakfast burritos, monsters, and learning how systems talk.
</div>
