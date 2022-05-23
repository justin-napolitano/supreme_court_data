using DataFrames
using CSV

function get_files(directory)
    file_name = String[]
    file_path = String[]

    working_path = joinpath(pwd(), directory)
    # context management.  Cd and then go back to the orignal pwd
    cd(working_path) do 
        #print("Current directory: ", working_path)
        foreach(readdir()) do f
            path = joinpath(working_path, f)
            push!(file_name,f)
            push!(file_path, path)
            #dump(stat(f.desc)) # you can customize what you want to print
        end
    end
    #println('\n', pwd())
    #display(file_paths)
    file_name = sort_array(file_name)
    file_path = sort_array(file_path)
    df = DataFrame(File = file_name, Path = file_path)
    return df

end



function sort_array(array)
    
    return sort(array; alg=MergeSort)

end



function df_to_file(df,outpath)
    CSV.write(outpath, df)
    return outpath

end


function main()
    
    # outpath fo the current file
    outpath = joinpath(pwd(),"case_files.csv")

    #Glob files from directory
    oyez_dataframe = get_files("oyez_cited")
    
    #Glob files from directory
    loc_dataframe = get_files("loc_cited")

    
    # Join on File excluding extraneous data not in the oyez dataset
    master_df = innerjoin(oyez_dataframe, loc_dataframe, on = :File, validate=(true, true), makeunique = true)

    #Select every file but the .DS_Store from the dataframe.  
    master_df = filter(row -> !(row.File == ".DS_Store"), master_df)

    #Write to file
    outpath = df_to_file(master_df,outpath)
    

end

main()

