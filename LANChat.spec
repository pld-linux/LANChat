Summary:	LANChat - network-chatting program
Summary(pl.UTF-8):	LANChat - program do sieciowych pogaduszek
Name:		LANChat
Version:	1.1.0
Release:	3
License:	GPL
Group:		Applications/Networking
Source0:	http://republika.pl/lanchat/%{name}-%{version}.tar.gz
# Source0-md5:	efa396cbe01c1c63e69192ea64dbb407
URL:		http://republika.pl/lanchat/
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

%description -l pl.UTF-8
LANChat jest programem do sieciowych pogaduszek. Pozwala na
rozmawianie ze swoimi znajomymi w sieciach lokalnych opartych na
TCP/IP. Nie potrzebuje żadnego serwera do działania i każdy użytkownik
jest równy. Nie jest to aplikacja typu klient-serwer, więc każda
maszyna jest jak niezależny serwer. LANChat do komunikacji używa
broadcastów UDP, więc nie są one wysyłane do internetu, a tylko do
najbliższego routera. LANChat potrzebuje klasy adresowej C
(teoretycznie max 254 użytkowników). Używając LANChata można
rozmawiać w swojej sieci lokalnej zarówno z użytkownikami Windows jak
i Linuksa. Można też korzystać z LANChata w sieciach połączonych
BRIDGE'ami.

%prep
%setup -q -c -T
tar zxf %{SOURCE0} -C ..
cd ..
chmod u+x %{name}-%{version}

%build
%{__make} CC="%{__cc} %{rpmcflags} -Wall -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install LANChat $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ROUTING BUGS TODO
%attr(755,root,root) %{_bindir}/LANChat
