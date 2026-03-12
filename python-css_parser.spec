%define oname css_parser
%define module css-parser

Name:		python-%{oname}
Version:	1.0.10
Release:	1
Summary:	Python module for parsing and building CSS 
Group:		Development/Python
License:	LGPL-3.0-or-later
URL:		https://pypi.org/project/css-parser
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch 
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
cssutils is a Python module for building and parsing CSS (Cascading
Style Sheets).

%prep -a
# Remove bundled egg-info
rm -rf src/%{oname}.egg-info
# Fix interpreter
find -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python|#!%{__python3}|'
# Fix non-executable scripts
sed -i "1d" src/css_parser/{parse,codec,sac,serialize,scripts/csscapture,_codec2,errorhandler,scripts/cssparse,_codec3,scripts/csscombine,tokenize2,version,encutils/__init__,__init__}.py

%files
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{oname}-%{version}-py%{py_ver}.egg-info
