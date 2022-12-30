# Jan -> January
# Feb -> February
#dictionaries should be def with {}, key value pairs are only accepted, keys should be unique no duplicates

month_conversion ={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
    0:"Demo"
}

print(month_conversion["Nov"])#1 way 2 access
print(month_conversion.get("Mar"))
print(month_conversion.get("blah", "Invalid key"))#default value to fall back on

print(month_conversion[0])