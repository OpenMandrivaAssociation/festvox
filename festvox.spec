%define name festvox
%define version 1.4.3
%define release %mkrel 4

Name:  		%name
Summary: 	Voices for Festival - a free speech synthesizer 
Version: 	%{version}
Release: 	%release
License: 	BSD
Group: 		Sound
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root 
URL: 		http://www.cstr.ed.ac.uk/projects/festival/
BuildArch: 	noarch

### VOICES
# American English male speaker (KAL), residual excited LPC diphone database
Source200: 	ftp://ftp.cstr.ed.ac.uk/pub/festival/%{version}/festvox_kallpc16k.tar.bz2
# Same voice at lower quality
Source201: 	ftp://ftp.cstr.ed.ac.uk/pub/festival/%{version}/festvox_kallpc8k.tar.bz2
# American English male speaker, residual excited LPC diphone database
Source202: 	ftp://ftp.cstr.ed.ac.uk/pub/festival/%{version}/festvox_kedlpc16k.tar.bz2
# Same voice at lower quality
Source203: 	ftp://ftp.cstr.ed.ac.uk/pub/festival/%{version}/festvox_kedlpc8k.tar.bz2
# British English RP male speaker using residual excited LPC diphone
# database, requires festlex_POSLEX and festlex_OALD (non-free)
#Source204: 	ftp://ftp.cstr.ed.ac.uk/pub/festival/%{version}/festvox_rablpc16k.tar.bz2
# Same as festvox_rablpc16k but at 8KHz sampling.
# requires festlex_POSLEX and festlex_OALD (non-free)
#Source205: 	ftp://ftp.cstr.ed.ac.uk/pub/festival/%{version}/festvox_rablpc8k.tar.bz2 

# Castilian Spanish male speaker, residual excited LPC diphone database
# NONFREE! - Free for non-commercial use
#Source299: 	ftp://ftp.cstr.ed.ac.uk/pub/festival/%{version}/festvox_ellpc11k.tar.bz2

# Add some useful words to the dictionary...
#Patch10: CMU-redhat.patch.bz2

%description
Festival is a general multi-lingual speech synthesis system developed
at CSTR. It offers a full text to speech system with various APIs, as
well as an environment for development and research of speech synthesis
techniques. It is written in C++ with a Scheme-based command interpreter
for general control.

This package contains voices for use with Festival


%package kallpc16k
Group:		Sound
Summary:	Festival Voice - American English male speaker (KAL) 16kHz
Requires:	festvox-kallpc-common
Provides:	festival-voice
Provides:	festival-voice-english
Provides:	festival-voice-en_US

%description kallpc16k
Festival Voice - American English male speaker (KAL) 16kHz

%package kallpc8k
Group:		Sound
Summary:	Festival Voice - American English male speaker (KAL) 8kHz
Requires:	festvox-kallpc-common
Provides:	festival-voice
Provides:	festival-voice-english
Provides:	festival-voice-en_US

%description kallpc8k
Festival Voice - American English male speaker (KAL) 8kHz

%package kallpc-common
Group:		Sound
Summary:	Festival Voice - American English male speaker (KAL) - Common
Requires:	festlex-CMU

%description kallpc-common
Festival Voice - American English male speaker (KAL)

Files shared between the 16kHz and 8kHz Voices


%package kedlpc16k
Group:		Sound
Summary:	Festival Voice - American English male speaker (KED) 16kHz
Requires:	festvox-kedlpc-common
Provides:	festival-voice
Provides:	festival-voice-english
Provides:	festival-voice-en_US

%description kedlpc16k
Festival Voice - American English male speaker (KAL) 16kHz

%package kedlpc8k
Group:		Sound
Summary:	Festival Voice - American English male speaker (KDE) 8kHz
Requires:	festvox-kedlpc-common
Provides:	festival-voice
Provides:	festival-voice-english
Provides:	festival-voice-en_US

%description kedlpc8k
Festival Voice - American English male speaker (KED) 8kHz

%package kedlpc-common
Group:		Sound
Summary:	Festival Voice - American English male speaker (KED) - Common
Requires:	festlex-CMU

%description kedlpc-common
Festival Voice - American English male speaker (KED)

Files shared between the 16kHz and 8kHz Voices


#%package rablpc16k
#Group:		Sound
#Summary:	Festival Voice - British English male speaker (RAB) 16kHz
#Requires:	festvox-rablpc-common
#Provides:	festival-voice
#Provides:	festival-voice-english
#Provides:	festival-voice-en_UK

#%description rablpc16k
#Festival Voice - British English male speaker (RAB) 16kHz

#%package rablpc8k
#Group:		Sound
#Summary:	Festival Voice - British English male speaker (RAB) 8kHz
#Requires:	festvox-rablpc-common
#Provides:	festival-voice
#Provides:	festival-voice-english
#Provides:	festival-voice-en_UK

#%description rablpc8k
#Festival Voice - American English male speaker (RAB) 8kHz

#%package rablpc-common
#Group:		Sound
#Summary:	Festival Voice - British English male speaker (RAB) - Common
#Requires:	festlex-OALD

#%description rablpc-common
#Festival Voice - British English male speaker (RAB)

#Files shared between the 16kHz and 8kHz Voices

%prep
rm -rf $RPM_BUILD_ROOT

#%setup -D -T -c -q -a 100 -a 101 -a 201 -a 202 -a 203 -a 204 -a205
%setup  -T -c -q -a 200 -a 201 -a 202 -a 203
#%patch10

%build

#cd festival/lib/dicts/cmu
#make
#cd ../../..

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/festival
cp -a festival/lib/voices $RPM_BUILD_ROOT%_datadir/festival

rm -f $RPM_BUILD_ROOT/%{_datadir}/festival/voices/english/*/COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files kallpc16k
%defattr(-,root,root)
%_datadir/festival/voices/english/kal_diphone/group/kallpc16k.group

%files kallpc8k
%defattr(-,root,root)
%_datadir/festival/voices/english/kal_diphone/group/kallpc8k.group

%files kallpc-common
%defattr(-,root,root)
%doc festival/lib/voices/english/kal_diphone/COPYING
%_datadir/festival/voices/english/kal_diphone/festvox/*.scm

%files kedlpc16k
%defattr(-,root,root)
%_datadir/festival/voices/english/ked_diphone/group/kedlpc16k.group

%files kedlpc8k
%defattr(-,root,root)
%_datadir/festival/voices/english/ked_diphone/group/kedlpc8k.group

%files kedlpc-common
%defattr(-,root,root)
%doc festival/lib/voices/english/ked_diphone/COPYING
%_datadir/festival/voices/english/ked_diphone/festvox/*.scm

#%files rablpc16k
#%defattr(-,root,root)
#%_datadir/festival/voices/english/rab_diphone/group/rablpc16k.group

#%files rablpc8k
#%defattr(-,root,root)
#%_datadir/festival/voices/english/rab_diphone/group/rablpc8k.group

#%files rablpc-common
#%defattr(-,root,root)
#%doc festival/lib/voices/english/rab_diphone/COPYING
#%_datadir/festival/voices/english/rab_diphone/festvox/*.scm


