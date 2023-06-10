# List of functions that might cause Open Redirect vulnerabilities
open_redirect_functions = ["header(", "wp_redirect(", "wp_safe_redirect("]

# List of functions that might cause SQL injection vulnerabilities
sqli_functions = [
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
    "sqlite_single_query("
]

# List of functions that might cause Local File Inclusion (LFI) vulnerabilities
lfi_functions = [
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
]

# List of functions that might cause Server-Side Request Forgery (SSRF) vulnerabilities
ssrf_functions = ["file_get_contents(", "fopen(", "curl_init(", "curl_exec(", "curl_multi_exec", "curl_setopt(","wp_remote_get(", "wp_remote_post("]

# List of functions that might cause Remote Code Execution (RCE) vulnerabilities
rce_functions = [
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
    "pcntl_exec(",
]

# List of functions that might cause PHP Object Injection vulnerabilities
poi_functions = ["unserialize(","maybe_unserialize("]

# List of functions that might cause XXE vulnerabilities
xxe_functions = [
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
]


# List of functions that might cause XSS vulnerabilities (sinks)
xss_functions = ["echo", "print", "printf", "the_content(", "the_excerpt(", "the_title(", "comment_text(", "bloginfo(", "wp_title(", "get_the_author(", "get_comment_author_link(", "get_header(", "get_footer(", "get_sidebar(","document.write", "innerHTML"]

# List of functions that might cause SSTI vulnerabilities
ssti_functions = [
    # Render/Display methods
    "->render(",
    "view(",
    "->display(",
    "->execute(",
    "->draw(",
    "->get(",

    # Initialization
    "Twig\\Environment",
    "Smarty()",
    "Mustache_Engine",
    "League\\Plates\\Engine",
    "\\Phalcon\\Mvc\\View()",
    "Latte\\Engine",
    "PHPTAL(",
    "RainTPL",
    "Savant3()",
    "Dwoo\\Core()",
]


auth_functions=["add_action( 'wp_ajax_nopriv_"]
