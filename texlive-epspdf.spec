Name:		texlive-epspdf
Version:	66119
Release:	2
Summary:	Converter for PostScript, EPS and PDF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/epspdf
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epspdf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epspdf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-epspdf.bin = %{EVRD}

%description
Epspdf[tk] is a TeXlua script which converts between PostScript
or EPS and PDF. It has both a command-line and a GUI interface.
Using pdftops (from the xpdf command-line utilities) for round-
tripping opens up several new possibilities compared to older
similarly-named utilities.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/epspdf
%{_bindir}/epspdftk
%{_texmfdistdir}/scripts/epspdf
%doc %{_infodir}/epspdf.info*
%doc %{_texmfdistdir}/doc/support/epspdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/epspdf/epspdf.tlu epspdf
ln -sf %{_texmfdistdir}/scripts/epspdf/epspdftk.tcl epspdftk
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdistdir}/doc/info/*.info %{buildroot}%{_infodir}
