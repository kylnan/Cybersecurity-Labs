TARGET = retlib 

all: ${TARGET}

retlib: retlib.c
	gcc -m32 -fno-stack-protector -z noexecstack -o $@ $@.c
	sudo chown root $@ && sudo chmod 4755 $@

clean:
	rm -f *.o *.out ${TARGET} badfile
