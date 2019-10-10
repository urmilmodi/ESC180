################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Lectures/Lecture_13/fib.c 

OBJS += \
./Lectures/Lecture_13/fib.o 

C_DEPS += \
./Lectures/Lecture_13/fib.d 


# Each subdirectory must supply rules for building sources it contributes
Lectures/Lecture_13/%.o: ../Lectures/Lecture_13/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cygwin C Compiler'
	gcc -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


