Name:		texlive-epspdf
Version:	0.5.3
Release:	1
Summary:	Converter for PostScript, EPS and PDF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/epspdf
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epspdf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epspdf.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-epspdf.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Epspdf[tk] is a Ruby script which converts between PostScript,
EPS and PDF. It has both a command-line and a GUI interface.
Using pdftops (from the xpdf command-line utilities) for round-
tripping opens up several new possibilities compared to older
similarly-named utilities.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/epspdf
%{_bindir}/epspdftk
%{_texmfdistdir}/scripts/epspdf/epspdf.help
%{_texmfdistdir}/scripts/epspdf/epspdf.icns
%{_texmfdistdir}/scripts/epspdf/epspdf.ico
%{_texmfdistdir}/scripts/epspdf/epspdf.rb
%{_texmfdistdir}/scripts/epspdf/epspdfrc.rb
%{_texmfdistdir}/scripts/epspdf/epspdftk.tcl
%{_texmfdistdir}/scripts/epspdf/makegray.pro
%doc %{_texmfdistdir}/doc/support/epspdf/COPYING
%doc %{_texmfdistdir}/doc/support/epspdf/Changelog
%doc %{_texmfdistdir}/doc/support/epspdf/README
%doc %{_texmfdistdir}/doc/support/epspdf/default.css
%doc %{_texmfdistdir}/doc/support/epspdf/epspdf.install
%doc %{_texmfdistdir}/doc/support/epspdf/epspdf.pdf
%doc %{_texmfdistdir}/doc/support/epspdf/epspdf.texi
%doc %{_texmfdistdir}/doc/support/epspdf/images/cnv_osx.png
%doc %{_texmfdistdir}/doc/support/epspdf/images/config_lnx.png
%doc %{_texmfdistdir}/doc/support/epspdf/images/epspdf.png
%doc %{_texmfdistdir}/doc/support/epspdf/images/logo.pdf
%doc %{_texmfdistdir}/doc/support/epspdf/images/main_w32.png
%doc %{_texmfdistdir}/doc/support/epspdf/images/ps_settings.png
%doc %{_texmfdistdir}/doc/support/epspdf/index.html
%doc %{_texmfdistdir}/doc/support/epspdf/pstexi.tex
%doc %{_infodir}/epspdf.info*

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/epspdf/epspdf.rb epspdf
    ln -sf %{_texmfdistdir}/scripts/epspdf/epspdftk.tcl epspdftk
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdir}/doc/info/*.info %{buildroot}%{_infodir}
