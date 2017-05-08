#include <stdlib.h>
#include <ctype.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <time.h>

static char responses[255][20]; // record the responses. For science.

static char generic_strings_1[][80] = {
	"You are finally here!!",
	"Where have you been?!?",
	"Why are you here?",
	"What do you seek?",
	"How are doing?",
	"You are not wanted here"
};

static char generic_strings_2[][80] = {
	"That's horrible!",
	"...",
	"Really?!?",
	"STFU",
	"GO AWAY!!",
	"Aww... you're so nice",
	"Umm... that's ok",
	"Self destructing in 3..2..1..",
	"DANK!!",
	"Cool stuff",
	"Vim > Emacs",
	"... killed by 9",
	"All's well that ends",
	"Anything is possible, unless it's not",
	"What should I do?",
	"ad infinitum...",
	"Wait, what did she tell you?",
	"That's what she said",
	"You can solve and unsolve it at the same time",
	"You are always busy",
	"It's not easy to get this right anyway",
	"With firefox you can have private browsing with tracking protection",
	"How do you do?"
};

static char mesg[] = "Welcome Back!!";

#define ARRAY_SIZE(arr) (sizeof(arr)/sizeof(arr[0]))

int main()
{
 	char str[80];
 	char choice;
 	char offset;
 	int i;

 	srand(time(NULL));
 	/* setvbuf(stdin, 0, _IONBF, 0); */
 	setvbuf(stdout, 0, _IONBF, 0);

 	puts(mesg);

 	puts(generic_strings_1[rand()%ARRAY_SIZE(generic_strings_1)]);

 	printf("Tell me ALL about yourself: ");
 	fgets(str, 80, stdin);

 	puts(generic_strings_2[rand()%ARRAY_SIZE(generic_strings_2)]);

 	printf("Wanna chat? ");
 	while(isspace(choice=getchar()));

	offset = 0;
	while (choice == 'y') {
		printf("%s", "Say: ");
 		while(isspace(choice=getchar()));
 		ungetc(choice, stdin);
		fgets(responses[offset++], 20, stdin);

		i = rand()%ARRAY_SIZE(generic_strings_2);
		printf("%s\n", generic_strings_2[i]);

		printf("%s ", "More?");
 		while(isspace(choice=getchar()));
	}

 	printf("Goodbye ");
 	puts(str);
 	puts("\n\t\tSee you later...");

 	return 0;
}
