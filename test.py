#!/usr/bin/perl
use strict;
use warnings;

my $random_number = int(rand() + 0.5);

print $random_number, "\n";
exit $random_number;
