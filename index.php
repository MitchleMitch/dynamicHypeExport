<?php

// Define key-value mappings for scripts
$scriptMappings = array(
    "DCM" => "##WEBSITE##/pythonhoster/scripts/DCM.py",
    // Add more key-value mappings as needed
);

// Retrieve key from the request
$key = $_GET["key"];

// Check if the key exists in the mappings
if (array_key_exists($key, $scriptMappings)) {
    // Return the URL corresponding to the key
    echo $scriptMappings[$key];
} else {
    // Key not found, return an error or fallback URL
    echo "Key not found";
}

?>
