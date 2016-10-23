worktimes = [int(input()) for i in range(6)];
totalmins = sum(worktimes);
apt_in_mins = (int(input())*60) + int(input());
start_time_in_mins = apt_in_mins - totalmins;
sh, sm = divmod(start_time_in_mins, 60);
print(sh, sm);
