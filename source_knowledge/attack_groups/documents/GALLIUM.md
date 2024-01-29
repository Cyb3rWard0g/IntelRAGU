# GALLIUM - G0093

**Created**: 2019-07-18T20:47:50.050Z

**Modified**: 2022-08-12T21:26:22.303Z

**Contributors**: Daniyal Naeem, BT Security,Cybereason Nocturnus, @nocturnus

## Aliases

GALLIUM,Operation Soft Cell

## Description

[GALLIUM](https://attack.mitre.org/groups/G0093) is a cyberespionage group that has been active since at least 2012, primarily targeting telecommunications companies, financial institutions, and government entities in Afghanistan, Australia, Belgium, Cambodia, Malaysia, Mozambique, the Philippines, Russia, and Vietnam. Security researchers have identified [GALLIUM](https://attack.mitre.org/groups/G0093) as a likely Chinese state-sponsored group, based in part on tools used and TTPs commonly associated with Chinese threat actors.(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019)(Citation: Unit 42 PingPull Jun 2022)

## Techniques Used

|Matrix|Domain|Platform|Technique ID|Technique Name|Use|
| :---| :---| :---| :---| :---| :---|
|mitre-attack|enterprise-attack|PRE|T1583.004|Server|[GALLIUM](https://attack.mitre.org/groups/G0093) has used Taiwan-based servers that appear to be exclusive to [GALLIUM](https://attack.mitre.org/groups/G0093).(Citation: Microsoft GALLIUM December 2019)|
|mitre-attack|enterprise-attack|Linux,macOS,Windows|T1570|Lateral Tool Transfer|[GALLIUM](https://attack.mitre.org/groups/G0093) has used [PsExec](https://attack.mitre.org/software/S0029) to move laterally between hosts in the target network.(Citation: Microsoft GALLIUM December 2019)|
|mitre-attack|enterprise-attack|PRE|T1588.002|Tool|[GALLIUM](https://attack.mitre.org/groups/G0093) has used a variety of widely-available tools, which in some cases they modified to add functionality and/or subvert antimalware solutions.(Citation: Microsoft GALLIUM December 2019)|
|mitre-attack|enterprise-attack|macOS,Windows|T1553.002|Code Signing|[GALLIUM](https://attack.mitre.org/groups/G0093) has used stolen certificates to sign its tools including those from Whizzimo LLC.(Citation: Microsoft GALLIUM December 2019)|
|mitre-attack|enterprise-attack|Linux,macOS,Windows|T1041|Exfiltration Over C2 Channel|[GALLIUM](https://attack.mitre.org/groups/G0093) used Web shells and [HTRAN](https://attack.mitre.org/software/S0040) for C2 and to exfiltrate data.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Linux,macOS,Windows|T1027.005|Indicator Removal from Tools|[GALLIUM](https://attack.mitre.org/groups/G0093) ensured each payload had a unique hash, including by using different types of packers.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Windows|T1550.002|Pass the Hash|[GALLIUM](https://attack.mitre.org/groups/G0093) used dumped hashes to authenticate to other machines via pass the hash.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Linux,macOS,Windows,Network|T1005|Data from Local System|[GALLIUM](https://attack.mitre.org/groups/G0093) collected data from the victim's local system, including password hashes from the SAM hive in the Registry.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Linux,macOS,Windows,Network|T1018|Remote System Discovery|[GALLIUM](https://attack.mitre.org/groups/G0093) used a modified version of [NBTscan](https://attack.mitre.org/software/S0590) to identify available NetBIOS name servers over the network as well as <code>ping</code> to identify remote systems.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Windows,Linux,Containers,macOS|T1133|External Remote Services|[GALLIUM](https://attack.mitre.org/groups/G0093) has used VPN services, including SoftEther VPN, to access and maintain persistence in victim environments.(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019)|
|mitre-attack|enterprise-attack|Linux,macOS,Windows|T1560.001|Archive via Utility|[GALLIUM](https://attack.mitre.org/groups/G0093) used WinRAR to compress and encrypt stolen data prior to exfiltration.(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019)|
|mitre-attack|enterprise-attack|Linux,macOS,Windows|T1074.001|Local Data Staging|[GALLIUM](https://attack.mitre.org/groups/G0093) compressed and staged files in multi-part archives in the Recycle Bin prior to exfiltration.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Linux,macOS,Windows|T1027|Obfuscated Files or Information|[GALLIUM](https://attack.mitre.org/groups/G0093) used a modified version of [HTRAN](https://attack.mitre.org/software/S0040) in which they obfuscated strings such as debug messages in an apparent attempt to evade detection.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Linux,macOS,Windows|T1090.002|External Proxy|[GALLIUM](https://attack.mitre.org/groups/G0093) used a modified version of [HTRAN](https://attack.mitre.org/software/S0040) to redirect connections between networks.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|macOS,Windows,Linux|T1027.002|Software Packing|[GALLIUM](https://attack.mitre.org/groups/G0093) packed some payloads using different types of packers, both known and custom.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Windows|T1053.005|Scheduled Task|[GALLIUM](https://attack.mitre.org/groups/G0093) established persistence for [PoisonIvy](https://attack.mitre.org/software/S0012) by created a scheduled task.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Linux,macOS,Windows|T1036.003|Rename System Utilities|[GALLIUM](https://attack.mitre.org/groups/G0093) used a renamed cmd.exe file to evade detection.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Linux,macOS,Windows|T1105|Ingress Tool Transfer|[GALLIUM](https://attack.mitre.org/groups/G0093) dropped additional tools to victims during their operation, including portqry.exe, a renamed cmd.exe file, winrar, and [HTRAN](https://attack.mitre.org/software/S0040).(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019)|
|mitre-attack|enterprise-attack|Linux,macOS,Windows,Network|T1033|System Owner/User Discovery|[GALLIUM](https://attack.mitre.org/groups/G0093) used <code>whoami</code> and <code>query user</code> to obtain information about the victim user.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Windows,IaaS,Linux,macOS,Network|T1049|System Network Connections Discovery|[GALLIUM](https://attack.mitre.org/groups/G0093) used <code>netstat -oan</code> to obtain information about the victim network connections.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Linux,macOS,Windows,Network|T1016|System Network Configuration Discovery|[GALLIUM](https://attack.mitre.org/groups/G0093) used <code>ipconfig /all</code> to obtain information about the victim network configuration. The group also ran a modified version of [NBTscan](https://attack.mitre.org/software/S0590) to identify available NetBIOS name servers.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Windows|T1003.001|LSASS Memory|[GALLIUM](https://attack.mitre.org/groups/G0093) used a modified version of [Mimikatz](https://attack.mitre.org/software/S0002) along with a PowerShell-based [Mimikatz](https://attack.mitre.org/software/S0002) to dump credentials on the victim machines.(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019)|
|mitre-attack|enterprise-attack|Windows|T1003.002|Security Account Manager|[GALLIUM](https://attack.mitre.org/groups/G0093) used <code>reg</code> commands to dump specific hives from the Windows Registry, such as the SAM hive, and obtain password hashes.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Windows|T1059.003|Windows Command Shell|[GALLIUM](https://attack.mitre.org/groups/G0093) used the Windows command shell to execute commands.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Windows|T1047|Windows Management Instrumentation|[GALLIUM](https://attack.mitre.org/groups/G0093) used WMI for execution to assist in lateral movement as well as for installing tools across multiple assets.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Windows|T1059.001|PowerShell|[GALLIUM](https://attack.mitre.org/groups/G0093) used PowerShell for execution to assist in lateral movement as well as for dumping credentials stored on compromised machines.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Linux,Windows,macOS,Network|T1505.003|Web Shell|[GALLIUM](https://attack.mitre.org/groups/G0093) used Web shells to persist in victim environments and assist in execution and exfiltration.(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019)|
|mitre-attack|enterprise-attack|Windows,macOS,Linux|T1136.002|Domain Account|[GALLIUM](https://attack.mitre.org/groups/G0093) created high-privileged domain user accounts to maintain access to victim networks.(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019)|
|mitre-attack|enterprise-attack|Windows,Azure AD,Office 365,SaaS,IaaS,Linux,macOS,Google Workspace,Containers,Network|T1078|Valid Accounts|[GALLIUM](https://attack.mitre.org/groups/G0093) leveraged valid accounts to maintain access to a victim network.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Windows|T1574.002|DLL Side-Loading|[GALLIUM](https://attack.mitre.org/groups/G0093) used DLL side-loading to covertly load [PoisonIvy](https://attack.mitre.org/software/S0012) into memory on the victim machine.(Citation: Cybereason Soft Cell June 2019)|
|mitre-attack|enterprise-attack|Windows,IaaS,Network,Linux,macOS,Containers|T1190|Exploit Public-Facing Application|[GALLIUM](https://attack.mitre.org/groups/G0093) exploited a publicly-facing servers including Wildfly/JBoss servers to gain access to the network.(Citation: Cybereason Soft Cell June 2019)(Citation: Microsoft GALLIUM December 2019)|
