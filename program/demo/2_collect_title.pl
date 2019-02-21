use utf8;
use Encode;
use strict;
use warnings;
use URI::Escape;
use Time::HiRes qw(sleep);
use LWP::Simple;
use LWP::UserAgent;
use Mozilla::CA;
use Term::ANSIColor qw(:constants);
$Term::ANSIColor::AUTORESET = 1;
use Term::ANSIColor 2.00 qw(:pushpop);


my $option = 30;

#open(F, "know-how.csv")||die "cannot open input.csv':$!\n";
open(F, "3_DecideColor1221/know-how.csv")||die "cannot open input.csv':$!\n";
open(N, ">data/title.csv");
my $counter = 0;

while(my $list = <F>){
	chomp($list);
	my @n1  = split(/,/,$list);
	my $id  = $n1[0];
	my $htd = $n1[1];
	#my $eva = $n1[1];
	my $url = $n1[2];
	#my $true= $n1[2];
	my $pre = $n1[3];
	my $conf= $n1[4];
	#print BOLD GREEN $url."\n";
	my $html = get($url);


	if($html =~ '<meta property="og:site_name" content="'){
		my @n1 = split(/<meta property="og:site_name" content="/,$html,2);
		my $n2 = $n1[1];
		my @n3 = split(/"/,$n2,2);
		my $title = $n3[0];
		if($title =~ '｜'){
			my @n1 = split(/｜/,$title,2);
			$title = $n1[0];
		}
		#elsif($title =~ '（'){
		#	my @n1 = split(/（/,$title,2);
		#	my $n2 = $n1[1];
		#	my @n3 = split(/）/,$n2,2);
		#	$title = $n3[0];
		#}
		my $LEN = length($title);
		if($LEN > $option){
			$title = $url;
			$title =~ s/https:\/\///g;
			$title =~ s/http:\/\///g;
			$title =~ s/.com//g;
			$title =~ s/.co//g;
			$title =~ s/.jp//g;
			$title =~ s/www.//g;
			$title = uc $title;
		}
		print BOLD GREEN "No.".$counter."\t".encode('utf-8',$title)."\n";
		#print N $id.",".$eva.",".$url.",".encode('utf-8',$title)."\n";
		print N $id.",".$true.",".$url.",".encode('utf-8',$title).",".$pre.",".$conf."\n";
		#print length($title)."\n";
		$counter += 1;



	}else{
		my @n1 = split(/<title>/,$html,2);
		my $n2 = $n1[1];
		my @n3 = split(/<\/title>/,$n2,2);
		my $title = $n3[0];
		
		if($title =~ '\('){
			my @n4 = split(/\(/,$title,2);
			$title = $n4[0];
		}
		if($title =~ '（'){
			my @n4 = split(/（/,$title,2);
			$title = $n4[0];
		}
		if($title =~ '-'){
			my @n4 = split(/-/,$title,2);
			$title = $n4[0];
		}
		if($title =~ '｜'){
			my @n4 = split(/｜/,$title,2);
			$title = $n4[0];
		}
		if($title =~ '「'){
			my @n4 = split(/「/,$title,2);
			my $n5 = $n4[1];
			my @n6 = split(/」/,$n5,2);
			$title = $n6[0];
		}
		if($title =~ '【'){
			my @n4 = split(/【/,$title,2);
			my $n5 = $n4[1];
			my @n6 = split(/】/,$n5,2);
			$title = $n6[0];
		}
		if($title =~ ' '){
			my @n4 = split(/ /,$title,2);
			$title = $n4[0];
		}
		my $LEN = length($title);
		if($LEN > $option){
			$title = $url;
			$title =~ s/https:\/\///g;
			$title =~ s/http:\/\///g;
			$title =~ s/.com//g;
			$title =~ s/.co//g;
			$title =~ s/.jp//g;
			$title =~ s/www.//g;
			$title = uc $title;
		}
		print BOLD RED "No.".$counter."\t".encode('utf-8',$title)."\n";
		print N $id.",".$true.",".$url.",".encode('utf-8',$title).",".$pre.",".$conf."\n";
		#print N $id.",".$eva.",".$url.",".encode('utf-8',$title)."\n";
		#print length($title)."\n";
		$counter += 1;
	}
	sleep(0.5);
}

close(F);
close(N);
