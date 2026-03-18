.PHONY: create-practice remove-practice

create-practice:
ifndef NAME
	$(error NAME is not defined)
endif
	mkdir -p $(NAME)
	cp PracticeMakefile $(NAME)/Makefile

remove-practice:
ifndef NAME
	$(error NAME is not defined)
endif
	rm -rf $(NAME)

