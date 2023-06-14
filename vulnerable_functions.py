def get_vulnerable_functions(language):
    if language == "Python":
        return python_vulnerable_functions
    elif language == "JavaScript (Node.js)":
        return javascript_vulnerable_functions
    elif language == "Java":
        return java_vulnerable_functions
    elif language == "C#":
        return csharp_vulnerable_functions
    elif language == "PHP":
        return php_vulnerable_functions
    elif language == "Ruby":
        return ruby_vulnerable_functions
    elif language == "Go":
        return go_vulnerable_functions
    elif language == "Rust":
        return rust_vulnerable_functions
    elif language == "Swift":
        return swift_vulnerable_functions
    elif language == "Kotlin":
        return kotlin_vulnerable_functions
    elif language == "Scala":
        return scala_vulnerable_functions
    elif language == "Perl":
        return perl_vulnerable_functions
    elif language == "TypeScript (Node.js)":
        return typescript_vulnerable_functions
    elif language == "C++":
        return cpp_vulnerable_functions
    elif language == "Objective-C":
        return objc_vulnerable_functions
    else:
        return {}


# Python vulnerable functions
python_vulnerable_functions = {
    "Open Redirect": [
        # Add Python open redirect vulnerable functions here
    ],
    "SQL Injection": [
        # Add Python SQL injection vulnerable functions here
    ],
    "Local File Inclusion (LFI)": [
        # Add Python LFI vulnerable functions here
    ],
    "Server-Side Request Forgery (SSRF)": [
        # Add Python SSRF vulnerable functions here
    ],
    "Remote Code Execution (RCE)": [
        # Add Python RCE vulnerable functions here
    ],
    "Insecure Deserialization": [
        # Add Python insecure deserialization vulnerable functions here
    ],
    "XML External Entity (XXE)": [
        # Add Python XXE vulnerable functions here
    ],
    "Cross-Site Scripting (XSS)": [
        # Add Python XSS vulnerable functions here
    ],
    "Server-Side Template Injection (SSTI)": [
        # Add Python SSTI vulnerable functions here
    ],
    "Privilege Escalation": [
        # Add Python privilege escalation vulnerable functions here
    ]
}

# JavaScript (Node.js) vulnerable functions
javascript_vulnerable_functions = {
    "Open Redirect": [
        # Add JavaScript (Node.js) open redirect vulnerable functions here
    ],
    "SQL Injection": [
        # Add JavaScript (Node.js) SQL injection vulnerable functions here
    ],
    "Local File Inclusion (LFI)": [
        # Add JavaScript (Node.js) LFI vulnerable functions here
    ],
    "Server-Side Request Forgery (SSRF)": [
        # Add JavaScript (Node.js) SSRF vulnerable functions here
    ],
    "Remote Code Execution (RCE)": [
        # Add JavaScript (Node.js) RCE vulnerable functions here
    ],
    "Insecure Deserialization": [
        # Add JavaScript (Node.js) insecure deserialization vulnerable functions here
    ],
    "XML External Entity (XXE)": [
        # Add JavaScript (Node.js) XXE vulnerable functions here
    ],
    "Cross-Site Scripting (XSS)": [
        # Add JavaScript (Node.js) XSS vulnerable functions here
    ],
    "Server-Side Template Injection (SSTI)": [
        # Add JavaScript (Node.js) SSTI vulnerable functions here
    ],
    "Privilege Escalation": [
        # Add JavaScript (Node.js) privilege escalation vulnerable functions here
    ]
}


java_vulnerable_functions  = {
    
    "SQL Injection": [
        "execute(", "executeQuery(", "executeUpdate(", "addBatch(", "nativeSQL(", 
        "createNativeQuery(", "createQuery(", "update(", "query(", "selectList(", 
        "selectMap(", "selectOne(", "delete(", "insert(", "createSQLQuery("
    ],
    "XML External Entity (XXE)": [
        "newDocumentBuilder(", "newSAXParser(", "newXMLReader(", "newTransformer(", 
        "newSchema(", "newXPath(", "createXMLStreamReader(", "createXMLEventReader(", 
        "createXMLEventWriter(", "createXMLStreamWriter("
    ],
    "Insecure Deserialization": [
        "readObject(", "readUnshared(", "XMLDecoder(", "fromXML(", "readValue(", 
        "readObjectOrNull(", "copy(", "load(", "readObject(", "readArray(", "fromJson(", 
        "parseObject(", "unmarshal(", "parse(", "MappedXMLStreamReader(", "fromXML(", 
        "unmarshal(", "InvokerTransformer(", "DefaultMessageListenerContainer(", 
        "Interceptor(", "readElement("
    ],
    "Remote Code Execution (RCE)": [
        "exec(", "start(", "parse(", "execute(", "launch(", "executeCommand(", 
        "evaluate(", "me("
    ],
    "Server-Side Request Forgery (SSRF)": [
        "openConnection(", "send(", "getForObject(", "postForObject(", "exchange(", "execute("
    ],
    "Open Redirect": [
        "sendRedirect(", "setRedirectStrategy(", "setDefaultTargetURL("
    ],
    "Local File Inclusion (LFI)": [
        "getRealPath(", "getFile(", "getInputStream(", "load(", "copyToFile(", 
        "writeStringToFile(", "readFileToString("
    ],
    "Server-Side Template Injection (SSTI)": [
        "render(", "merge(",   
        "process(",                         
        "processTemplate(",                  
        "include(", "forward(",              
        "evaluate(",             
        "include(",                          
    ],
  "Cross-Site Scripting (XSS)": [
   ],
    "Privilege Escalation": [
    ]

    
}


# C# vulnerable functions
csharp_vulnerable_functions = {
    "Open Redirect": [
        # Add C# open redirect vulnerable functions here
    ],
    "SQL Injection": [
        # Add C# SQL injection vulnerable functions here
    ],
    "Local File Inclusion (LFI)": [
        # Add C# LFI vulnerable functions here
    ],
    "Server-Side Request Forgery (SSRF)": [
        # Add C# SSRF vulnerable functions here
    ],
    "Remote Code Execution (RCE)": [
        # Add C# RCE vulnerable functions here
    ],
    "Insecure Deserialization": [
        # Add C# insecure deserialization vulnerable functions here
    ],
    "XML External Entity (XXE)": [
        # Add C# XXE vulnerable functions here
    ],
    "Cross-Site Scripting (XSS)": [
        # Add C# XSS vulnerable functions here
    ],
    "Server-Side Template Injection (SSTI)": [
        # Add C# SSTI vulnerable functions here
    ],
    "Privilege Escalation": [
        # Add C# privilege escalation vulnerable functions here
    ]
}

# PHP vulnerable functions
php_vulnerable_functions = {
    "Open Redirect": [
        "header(",
        "wp_redirect(",
        "wp_safe_redirect("
    ],
    "SQL Injection": [
        "->query_posts(",
        "->get_results(",
        "->query(",
        "->get_var(",
        "->get_row(",
        "->get_col(",
        "->replace(",
        "mysqli_query(",
        "mysqli_real_query(",
        "pg_query(",
        "pg_send_query(",
        "sqlite_open(",
        "sqlite_query(",
        "sqlite_exec(",
        "sqlite_single_query(",
        "->select("
    ],
    "Local File Inclusion (LFI)": [
        "require(",
        "require_once(",
        "include(",
        "include_once(",
        "fread(",
        "unlink(",
        "readfile(",
        "file(",
        "file_get_contents(",
        "show_source(",
        "highlight_file("
    ],
    "Server-Side Request Forgery (SSRF)": [
        "file_get_contents(",
        "fopen(",
        "curl_init(",
        "curl_exec(",
        "curl_multi_exec",
        "curl_setopt(",
        "wp_remote_get(",
        "wp_remote_post("
    ],
    "Remote Code Execution (RCE)": [
        "eval(",
        "create_function(",
        "assert(",
        "file_put_contents(",
        "sanitize_file_name(",
        "php://input",
        "system(",
        "exec(",
        "shell_exec(",
        "passthru(",
        "popen(",
        "proc_open(",
        "pcntl_exec("
    ],
    "Insecure Deserialization": [
        "unserialize(",
        "maybe_unserialize("
    ],
    "XML External Entity (XXE)": [
        "simplexml_load_string(",
        "SimpleXMLElement(",
        "DOMDocument::loadXML(",
        "DOMDocument::loadHTML(",
        "DOMDocument::loadHTMLFile(",
        "xml_parse(",
        "xml_parse_into_struct(",
        "xml_parser_create_ns(",
        "xml_parser_create(",
        "XMLWriter::writeElement(",
        "XMLWriter::startElement(",
        "XMLWriter::writeElementNS(",
        "XMLWriter::startElementNS(",
        "XMLWriter::writeDTDElement("
    ],
    "Cross-Site Scripting (XSS)": [
        "echo",
        "print",
        "printf",
        "the_content(",
        "the_excerpt(",
        "the_title(",
        "comment_text(",
        "bloginfo(",
        "wp_title(",
        "get_the_author(",
        "get_comment_author_link(",
        "get_header(",
        "get_footer(",
        "get_sidebar(",
        "document.write",
        "innerHTML"
    ],
    "Server-Side Template Injection (SSTI)": [
        "->render(",
        "view(",
        "->display(",
        "->execute(",
        "->draw(",
        "->get(",
        "Twig\\Environment",
        "Smarty()",
        "Mustache_Engine",
        "League\\Plates\\Engine",
        "\\Phalcon\\Mvc\\View()",
        "Latte\\Engine",
        "PHPTAL(",
        "RainTPL",
        "Savant3()",
        "Dwoo\\Core()"
    ],
    "Privilege Escalation": [
        "add_action( 'wp_ajax_nopriv_"
    ]
}

# Ruby vulnerable functions
ruby_vulnerable_functions = {
    "Open Redirect": [
        # Add Ruby open redirect vulnerable functions here
    ],
    "SQL Injection": [
        # Add Ruby SQL injection vulnerable functions here
    ],
    "Local File Inclusion (LFI)": [
        # Add Ruby LFI vulnerable functions here
    ],
    "Server-Side Request Forgery (SSRF)": [
        # Add Ruby SSRF vulnerable functions here
    ],
    "Remote Code Execution (RCE)": [
        # Add Ruby RCE vulnerable functions here
    ],
    "Insecure Deserialization": [
        # Add Ruby insecure deserialization vulnerable functions here
    ],
    "XML External Entity (XXE)": [
        # Add Ruby XXE vulnerable functions here
    ],
    "Cross-Site Scripting (XSS)": [
        # Add Ruby XSS vulnerable functions here
    ],
    "Server-Side Template Injection (SSTI)": [
        # Add Ruby SSTI vulnerable functions here
    ],
    "Privilege Escalation": [
        # Add Ruby privilege escalation vulnerable functions here
    ]
}

# Go vulnerable functions
go_vulnerable_functions = {
    "Open Redirect": [
        # Add Go open redirect vulnerable functions here
    ],
    "SQL Injection": [
        # Add Go SQL injection vulnerable functions here
    ],
    "Local File Inclusion (LFI)": [
        # Add Go LFI vulnerable functions here
    ],
    "Server-Side Request Forgery (SSRF)": [
        # Add Go SSRF vulnerable functions here
    ],
    "Remote Code Execution (RCE)": [
        # Add Go RCE vulnerable functions here
    ],
    "Insecure Deserialization": [
        # Add Go insecure deserialization vulnerable functions here
    ],
    "XML External Entity (XXE)": [
        # Add Go XXE vulnerable functions here
    ],
    "Cross-Site Scripting (XSS)": [
        # Add Go XSS vulnerable functions here
    ],
    "Server-Side Template Injection (SSTI)": [
        # Add Go SSTI vulnerable functions here
    ],
    "Privilege Escalation": [
        # Add Go privilege escalation vulnerable functions here
    ]
}

# Rust vulnerable functions
rust_vulnerable_functions = {
    "Open Redirect": [
        # Add Rust open redirect vulnerable functions here
    ],
    "SQL Injection": [
        # Add Rust SQL injection vulnerable functions here
    ],
    "Local File Inclusion (LFI)": [
        # Add Rust LFI vulnerable functions here
    ],
    "Server-Side Request Forgery (SSRF)": [
        # Add Rust SSRF vulnerable functions here
    ],
    "Remote Code Execution (RCE)": [
        # Add Rust RCE vulnerable functions here
    ],
    "Insecure Deserialization": [
        # Add Rust insecure deserialization vulnerable functions here
    ],
    "XML External Entity (XXE)": [
        # Add Rust XXE vulnerable functions here
    ],
    "Cross-Site Scripting (XSS)": [
        # Add Rust XSS vulnerable functions here
    ],
    "Server-Side Template Injection (SSTI)": [
        # Add Rust SSTI vulnerable functions here
    ],
    "Privilege Escalation": [
        # Add Rust privilege escalation vulnerable functions here
    ]
}

# Swift vulnerable functions
swift_vulnerable_functions = {
    "Open Redirect": [
        # Add Swift open redirect vulnerable functions here
    ],
    "SQL Injection": [
        # Add Swift SQL injection vulnerable functions here
    ],
    "Local File Inclusion (LFI)": [
        # Add Swift LFI vulnerable functions here
    ],
    "Server-Side Request Forgery (SSRF)": [
        # Add Swift SSRF vulnerable functions here
    ],
    "Remote Code Execution (RCE)": [
        # Add Swift RCE vulnerable functions here
    ],
    "Insecure Deserialization": [
        # Add Swift insecure deserialization vulnerable functions here
    ],
    "XML External Entity (XXE)": [
        # Add Swift XXE vulnerable functions here
    ],
    "Cross-Site Scripting (XSS)": [
        # Add Swift XSS vulnerable functions here
    ],
    "Server-Side Template Injection (SSTI)": [
        # Add Swift SSTI vulnerable functions here
    ],
    "Privilege Escalation": [
        # Add Swift privilege escalation vulnerable functions here
    ]
}

# Kotlin vulnerable functions
kotlin_vulnerable_functions = {
    "Open Redirect": [
        # Add Kotlin open redirect vulnerable functions here
    ],
    "SQL Injection": [
        # Add Kotlin SQL injection vulnerable functions here
    ],
    "Local File Inclusion (LFI)": [
        # Add Kotlin LFI vulnerable functions here
    ],
    "Server-Side Request Forgery (SSRF)": [
        # Add Kotlin SSRF vulnerable functions here
    ],
    "Remote Code Execution (RCE)": [
        # Add Kotlin RCE vulnerable functions here
    ],
    "Insecure Deserialization": [
        # Add Kotlin insecure deserialization vulnerable functions here
    ],
    "XML External Entity (XXE)": [
        # Add Kotlin XXE vulnerable functions here
    ],
    "Cross-Site Scripting (XSS)": [
        # Add Kotlin XSS vulnerable functions here
    ],
    "Server-Side Template Injection (SSTI)": [
        # Add Kotlin SSTI vulnerable functions here
    ],
    "Privilege Escalation": [
        # Add Kotlin privilege escalation vulnerable functions here
    ]
}

# Scala vulnerable functions
scala_vulnerable_functions = {
    "Open Redirect": [
        # Add Scala open redirect vulnerable functions here
    ],
    "SQL Injection": [
        # Add Scala SQL injection vulnerable functions here
    ],
    "Local File Inclusion (LFI)": [
        # Add Scala LFI vulnerable functions here
    ],
    "Server-Side Request Forgery (SSRF)": [
        # Add Scala SSRF vulnerable functions here
    ],
    "Remote Code Execution (RCE)": [
        # Add Scala RCE vulnerable functions here
    ],
    "Insecure Deserialization": [
        # Add Scala insecure deserialization vulnerable functions here
    ],
    "XML External Entity (XXE)": [
        # Add Scala XXE vulnerable functions here
    ],
    "Cross-Site Scripting (XSS)": [
        # Add Scala XSS vulnerable functions here
    ],
    "Server-Side Template Injection (SSTI)": [
        # Add Scala SSTI vulnerable functions here
    ],
    "Privilege Escalation": [
        # Add Scala privilege escalation vulnerable functions here
    ]
}

# Perl vulnerable functions
perl_vulnerable_functions = {
    "Open Redirect": [
        # Add Perl open redirect vulnerable functions here
    ],
    "SQL Injection": [
        # Add Perl SQL injection vulnerable functions here
    ],
    "Local File Inclusion (LFI)": [
        # Add Perl LFI vulnerable functions here
    ],
    "Server-Side Request Forgery (SSRF)": [
        # Add Perl SSRF vulnerable functions here
    ],
    "Remote Code Execution (RCE)": [
        # Add Perl RCE vulnerable functions here
    ],
    "Insecure Deserialization": [
        # Add Perl insecure deserialization vulnerable functions here
    ],
    "XML External Entity (XXE)": [
        # Add Perl XXE vulnerable functions here
    ],
    "Cross-Site Scripting (XSS)": [
        # Add Perl XSS vulnerable functions here
    ],
    "Server-Side Template Injection (SSTI)": [
        # Add Perl SSTI vulnerable functions here
    ],
    "Privilege Escalation": [
        # Add Perl privilege escalation vulnerable functions here
    ]
}

# TypeScript (Node.js) vulnerable functions
typescript_vulnerable_functions = {
    "Open Redirect": [
        # Add TypeScript (Node.js) open redirect vulnerable functions here
    ],
    "SQL Injection": [
        # Add TypeScript (Node.js) SQL injection vulnerable functions here
    ],
    "Local File Inclusion (LFI)": [
        # Add TypeScript (Node.js) LFI vulnerable functions here
    ],
    "Server-Side Request Forgery (SSRF)": [
        # Add TypeScript (Node.js) SSRF vulnerable functions here
    ],
    "Remote Code Execution (RCE)": [
        # Add TypeScript (Node.js) RCE vulnerable functions here
    ],
    "Insecure Deserialization": [
        # Add TypeScript (Node.js) insecure deserialization vulnerable functions here
    ],
    "XML External Entity (XXE)": [
        # Add TypeScript (Node.js) XXE vulnerable functions here
    ],
    "Cross-Site Scripting (XSS)": [
        # Add TypeScript (Node.js) XSS vulnerable functions here
    ],
    "Server-Side Template Injection (SSTI)": [
        # Add TypeScript (Node.js) SSTI vulnerable functions here
    ],
    "Privilege Escalation": [
        # Add TypeScript (Node.js) privilege escalation vulnerable functions here
    ]
}

# C++ vulnerable functions
cpp_vulnerable_functions = {
    "Open Redirect": [
        # Add C++ open redirect vulnerable functions here
    ],
    "SQL Injection": [
        # Add C++ SQL injection vulnerable functions here
    ],
    "Local File Inclusion (LFI)": [
        # Add C++ LFI vulnerable functions here
    ],
    "Server-Side Request Forgery (SSRF)": [
        # Add C++ SSRF vulnerable functions here
    ],
    "Remote Code Execution (RCE)": [
        # Add C++ RCE vulnerable functions here
    ],
    "Insecure Deserialization": [
        # Add C++ insecure deserialization vulnerable functions here
    ],
    "XML External Entity (XXE)": [
        # Add C++ XXE vulnerable functions here
    ],
    "Cross-Site Scripting (XSS)": [
        # Add C++ XSS vulnerable functions here
    ],
    "Server-Side Template Injection (SSTI)": [
        # Add C++ SSTI vulnerable functions here
    ],
    "Privilege Escalation": [
        # Add C++ privilege escalation vulnerable functions here
    ]
}

# Objective-C vulnerable functions
objc_vulnerable_functions = {
    "Open Redirect": [
        # Add Objective-C open redirect vulnerable functions here
    ],
    "SQL Injection": [
        # Add Objective-C SQL injection vulnerable functions here
    ],
    "Local File Inclusion (LFI)": [
        # Add Objective-C LFI vulnerable functions here
    ],
    "Server-Side Request Forgery (SSRF)": [
        # Add Objective-C SSRF vulnerable functions here
    ],
    "Remote Code Execution (RCE)": [
        # Add Objective-C RCE vulnerable functions here
    ],
    "Insecure Deserialization": [
        # Add Objective-C insecure deserialization vulnerable functions here
    ],
    "XML External Entity (XXE)": [
        # Add Objective-C XXE vulnerable functions here
    ],
    "Cross-Site Scripting (XSS)": [
        # Add Objective-C XSS vulnerable functions here
    ],
    "Server-Side Template Injection (SSTI)": [
        # Add Objective-C SSTI vulnerable functions here
    ],
    "Privilege Escalation": [
        # Add Objective-C privilege escalation vulnerable functions here
    ]
}
