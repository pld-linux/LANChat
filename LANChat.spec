Summary:	LANChat - network-chatting program
Summary(pl):	LANChat
Name:		LANChat
Version:	1.0.2
Release:	1
License:	GPL
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Group(de):	Applikationen/Netzwerkwesen
Source0:	http://priv4.onet.pl./ki/lanchat/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_am.patch
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
LANChat

%prep
%setup -q 
%patch0 -p1

%build
libtoolize --copy --force
aclocal
automake -a -c
autoconf
CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS} -I/usr/include/ncurses"
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
