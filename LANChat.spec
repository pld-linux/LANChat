Summary:	LANChat - network-chatting program
Summary(pl):	LANChat - program do sieciowych pogaduszek
Name:		LANChat
Version:	1.0.2
Release:	4
License:	GPL
Group:		Applications/Networking
Source0:	http://priv4.onet.pl./ki/lanchat/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_am.patch
Patch1:		%{name}-wincrash.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LANChat a network-chatting program. It allows you to chat with your
friends over a TCP/IP based Local Area Network. It doesn't need any
type of server to run. All users are equal. LANChat is a not
client-server application. All your machines act like independent
servers. To communicate LANChat uses broadcast UDP messages so they
don't travel over the Internet (only to the closest router). LANChat
need C-class addressing type (theoretically max 254 users). By using
LANChat you can talk with windows and Linux users in your local area
network. You can use LANChat over networks connected by the BRIDGE.

%description -l pl
LANChat jest programem do sieciowych pogaduszek. Pozwala na
rozmawianie ze swoimi znajomymi w sieciach lokalnych opartych na
TCP/IP. Nie potrzebuje ¿adnego servera do dzia³ania i ka¿dy u¿ytkownik
jest równy. Nie jest to aplikacja typu klient-server, wiêc ka¿da
maszyna jest jak niezale¿ny server. LANChat do komunikacji u¿ywa
broadcastów UDP, wiêc nie s± one wysy³ane do internetu, a tylko do
najbli¿szego routera. LANChat potrzebuje klasy adresowej C
(teoretycznie max 254 u¿ytkowników). U¿ywaj±c LANChata mo¿esz
rozmawiaæ w swojej sieci lokalnej zarówno z u¿ytkownikami Windows jak
i Linuksa. Mo¿esz te¿ korzystaæ z LANChata w sieciach po³±czonych
BRIDGE'ami.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf NEWS README ROUTING BUGS TODO lanchat.lsm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/LANChat
