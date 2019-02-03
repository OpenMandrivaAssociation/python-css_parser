%define oname	css_parser
%define name	python-%{oname}

Name:		%{name}
Version:	1.0.4
Release:	1
Summary:	Python module for parsing and building CSS 
Group:		Development/Python
License:	LGPLv3+
URL:		https://pypi.org/project/css-parser
Source0:	https://files.pythonhosted.org/packages/38/97/94c9cdb2410d4f89749fa947338970203ef26f2bdb7ac089ab96a87763d2/css-parser-%{version}.tar.gz
BuildArch:	noarch 
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
  
%description 
cssutils is a Python module for building and parsing CSS (Cascading
Style Sheets).
 
%package -n python2-%{oname}
Summary:	Python 2 module for parsing and building CSS 
Group:		Development/Python

%description -n python2-%{oname}
cssutils is a Python module for building and parsing CSS (Cascading
Style Sheets).

%prep
%autosetup -n css-parser-%{version}
cp -a . %{py2dir}

%build 

%install 
pushd %{py2dir}
python2 setup.py install --root=%{buildroot} --compile --optimize=2
popd

python setup.py install --root=%{buildroot} --compile --optimize=2

%files  
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{oname}-%{version}-py%{py_ver}.egg-info
# %{py_puresitedir}/tests/*py
# %{py_puresitedir}/tests/test_encutils/*py

%files -n python2-%{oname}
%{py2_puresitedir}/%{oname}
%{py2_puresitedir}/%{oname}-%{version}-py%{py2_ver}.egg-info
